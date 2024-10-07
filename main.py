import dearpygui.dearpygui as dpg
import opengate as gate
from view import *

simulation: gate.Simulation

def create_simulation_manager():
    global simulation
    name = dpg.get_value("user_info_name")
    simulation = gate.Simulation(name)

    user_info: {str: ()} = simulation.user_info

    user_info['verbose_level'] = dpg.get_value("user_info_verbose_level")
    user_info['running_verbose_level'] = int(dpg.get_value("user_info_running_verbose_level"))
    if dpg.get_value("user_info_g4_verbose"):
        user_info['g4_verbose'] = dpg.get_value("user_info_g4_verbose")
        user_info['g4_verbose_level'] = int(dpg.get_value("user_info_g4_verbose_level"))
    user_info['visu'] = dpg.get_value("user_info_visu")
    user_info['random_engine'] = dpg.get_value("user_info_random_engine")
    if dpg.get_value("user_info_random_seed") != "auto":
        user_info['random_seed'] = int(dpg.get_value("user_info_random_seed"))

    simulation.volume_manager.world_volume.size = [dpg.get_value("world_volume_size")] * 3 # [x, y, z]

    dpg.set_value("status_text", "Simulation successfully created!")
    dpg.configure_item("next_button", show=True)

def run_simulation():
    global simulation
    try:
        simulation.run(True)
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
    size = [dpg.get_value("volume_size")] * 3 # [x, y, z]

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


def read_volume():
    pass


def update_volume():
    pass


def delete_volume():
    pass


if __name__ == "__main__":
    view()
