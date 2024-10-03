import dearpygui.dearpygui as dpg
import opengate as gate


simulation: gate.Simulation

def main():
    dpg.create_context()
    dpg.create_viewport(title="Gate wrapper", width=800, height=600)

    # Simulation Manager window
    with dpg.window(label="1. Simulation Manager", width=600, height=400):
        dpg.add_text("Step 1")
        dpg.add_input_text(label="Simulation name", tag="user_info_name", default_value="simulation")

        with dpg.collapsing_header(label="GATE Verbosity"):
            dpg.add_combo(label="Verbose level", tag="user_info_verbose_level", items=["NONE", "INFO", "DEBUG"], default_value="INFO")
            dpg.add_combo(label="Running verbose level", tag="user_info_running_verbose_level", items=["0", "1", "2"], default_value="0")

        with dpg.collapsing_header(label="Geant4 Verbosity"):
            dpg.add_checkbox(label="Geant4 verbose system", tag="user_info_g4_verbose", default_value=False)
            dpg.add_combo(label="Geant4 verbose level", tag="user_info_g4_verbose_level", items=["0", "1", "2"], default_value="0")

        dpg.add_checkbox(label="Visualisation", tag="user_info_visu", default_value=False)

        with dpg.collapsing_header(label="Random Number Generator"):
            dpg.add_combo(label="Random engine", tag="user_info_random_engine", items=["MixMaxRng", "MersenneTwister"], default_value="MersenneTwister")
            dpg.add_input_text(label="Random seed", tag="user_info_random_seed", default_value="auto")

        dpg.add_button(label="Create Simulation", callback=create_simulation_manager)

        # Sub-managers: physics, actor and source

        dpg.add_text("Step 2")
        dpg.add_button(label="Run Simulation", callback=run_simulation)
        dpg.add_text("Status: ", tag="status_text")

    # Volume Manager window
    with dpg.window(label="2. Volume Manager", width=600, height=400):
        with dpg.table(tag="volume_table", header_row=True):
            dpg.add_table_column(label="Volume Name")

        dpg.add_button(label="List Volumes", callback=list_volumes)

        dpg.add_combo(label="Volume type", tag="volume_type", items=["Box", "Sphere"], default_value="Box")
        dpg.add_input_text(label="Volume name", tag="volume_name")
        dpg.add_combo(label="Volume material", tag="volume_material", items=["G4_WATER", "G4_AIR"], default_value="G4_WATER")

        dpg.add_slider_float(label="Volume size (mm)", tag="volume_size", min_value=1.0, max_value=100.0, default_value=50.0)

        dpg.add_slider_float(label="Position X", tag="volume_position_x", min_value=-100.0, max_value=100.0, default_value=0.0)
        dpg.add_slider_float(label="Position Y", tag="volume_position_y", min_value=-100.0, max_value=100.0, default_value=0.0)
        dpg.add_slider_float(label="Position Z", tag="volume_position_z", min_value=-100.0, max_value=100.0, default_value=0.0)

        dpg.add_button(label="Create Volume", callback=create_volume)
        dpg.add_button(label="Update Volume", callback=update_volume)
        dpg.add_button(label="Delete Volume", callback=delete_volume)
        dpg.add_text("Volume Status: ", tag="volume_status")

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


def create_simulation_manager():
    # Basic simulation setup and configuration
    name = dpg.get_value("user_info_name")
    global simulation
    simulation = gate.Simulation(name)

    # Setting simulation parameters from user input
    user_info = simulation.user_info
    user_info['verbose_level'] = dpg.get_value("user_info_verbose_level")
    user_info['running_verbose_level'] = int(dpg.get_value("user_info_running_verbose_level"))
    if dpg.get_value("user_info_g4_verbose"):
        user_info['g4_verbose'] = dpg.get_value("user_info_g4_verbose")
        user_info['g4_verbose_level'] = int(dpg.get_value("user_info_g4_verbose_level"))
    user_info['visu'] = dpg.get_value("user_info_visu")
    user_info['random_engine'] = dpg.get_value("user_info_random_engine")
    if dpg.get_value("user_info_random_seed") != "auto":
        user_info['random_seed'] = int(dpg.get_value("user_info_random_seed"))
    simulation.user_info = user_info

def run_simulation():
    try:
        simulation.run()
        dpg.set_value("status_text", "Status: Simulation Complete!")
    except Exception as e:
        dpg.set_value("status_text", f"Status: Simulation Failed! Error: {str(e)}")


def create_volume():
    global simulation
    if simulation is None:
        dpg.set_value("volume_status", "Error: Simulation not initialized!")
        return

    # Retrieve volume details from the GUI
    volume_name = dpg.get_value("volume_name").strip()
    if not volume_name:
        dpg.set_value("volume_status", "Error: Volume name is required!")
        return

    volume_type = dpg.get_value("volume_type")
    volume_material = dpg.get_value("volume_material")
    size = [dpg.get_value("volume_size")] * 3

    pos_x = dpg.get_value("volume_position_x")
    pos_y = dpg.get_value("volume_position_y")
    pos_z = dpg.get_value("volume_position_z")

    try:
        # Access volume_manager from the simulation object
        volume_manager = simulation.volume_manager
        volume = volume_manager.add_volume(volume_type, volume_name)
        volume.material = volume_material
        volume.size = size
        volume.translation = [pos_x, pos_y, pos_z]

        dpg.set_value("volume_status", f"Volume '{volume_name}' created successfully.")
    except Exception as e:
        dpg.set_value("volume_status", f"Error creating volume: {str(e)}")


def list_volumes():
    global simulation
    if simulation is None:
        dpg.set_value("volume_status", "Error: Simulation not initialized!")
        return

    try:
        volume_manager = simulation.volume_manager
        volumes = volume_manager.volumes  # Ensure this returns a dict or list of volume names

        # Clear previous list if exists
        if dpg.does_item_exist("volume_table"):
            dpg.delete_item("volume_table", children_only=True)

        # Add volumes to the table dynamically
        for vol_name in volumes:
            with dpg.table_row(parent="volume_table"):
                dpg.add_text(vol_name)

    except Exception as e:
        dpg.set_value("volume_status", f"Error retrieving volumes: {str(e)}")


def select_volume(sender, app_data, user_data):
    volume_name = user_data
    load_volume_details(volume_name)


def load_volume_details(volume_name):
    global simulation
    volume_manager = simulation.volume_manager
    volume = volume_manager.get_volume(volume_name)

    # Assuming the volume object has size and translation attributes
    dpg.set_value("volume_name", volume_name)
    dpg.set_value("volume_size", volume.size[0])  # Adjust for box shape
    dpg.set_value("volume_position_x", volume.translation[0])
    dpg.set_value("volume_position_y", volume.translation[1])
    dpg.set_value("volume_position_z", volume.translation[2])

def update_volume():
    # Placeholder logic for updating volumes
    dpg.set_value("volume_status", "Volume Updated")


def delete_volume():
    # Placeholder logic for deleting volumes
    dpg.set_value("volume_status", "Volume Deleted")


if __name__ == "__main__":
    main()
