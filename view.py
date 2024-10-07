from main import *
import dearpygui.dearpygui as dpg

def toggle_advanced_options(show):
    dpg.configure_item("advanced_options", show=show)

def next_step():
    dpg.delete_item("simulation_setup_window")

    simulation_editor()

def simulation_setup():
    with dpg.window(label="Simulation Setup", tag="simulation_setup_window", width=-1, height=-1, pos=(0, 0)):
        dpg.add_text("Simulation Setup", color=(0, 255, 0))

        dpg.add_input_text(label="Simulation name", tag="user_info_name", default_value="simulation")

        dpg.add_checkbox(label="Show Advanced Options", tag="advanced_options_toggle", callback=lambda: toggle_advanced_options(dpg.get_value("advanced_options_toggle")))
        with dpg.group(tag="advanced_options", show=False):
            dpg.add_text("Advanced Options", color=(0, 255, 0))

            dpg.add_checkbox(label="Visualisation", tag="user_info_visu", default_value=False)

            with dpg.collapsing_header(label="GATE Verbosity"):
                dpg.add_combo(label="Verbose level", tag="user_info_verbose_level", items=["NONE", "INFO", "DEBUG"], default_value="INFO")
                dpg.add_tooltip("Verbose level: NONE (no output), INFO (basic info), DEBUG (detailed info)")

                dpg.add_combo(label="Running verbose level", tag="user_info_running_verbose_level", items=["0", "1", "2"], default_value="0")
                dpg.add_tooltip("Running verbose level: 0 (minimal), 1 (moderate), 2 (detailed)")

            with dpg.collapsing_header(label="Geant4 Verbosity"):
                dpg.add_checkbox(label="Geant4 verbose system", tag="user_info_g4_verbose", default_value=False)
                dpg.add_combo(label="Geant4 verbose level", tag="user_info_g4_verbose_level", items=["0", "1", "2"], default_value="0")

            with dpg.collapsing_header(label="Random Number Generator"):
                dpg.add_combo(label="Random engine", tag="user_info_random_engine", items=["MixMaxRng", "MersenneTwister"], default_value="MersenneTwister")
                dpg.add_input_text(label="Random seed", tag="user_info_random_seed", default_value="auto")

        dpg.add_slider_int(label="World Box Size", tag="world_volume_size", min_value=-0, max_value=100, default_value=50)

        dpg.add_button(label="Create Simulation", callback=create_simulation_manager)
        dpg.add_text("Status: create a simulation!", tag="status_text", color=(255, 255, 0))

        # "Next" button will only be shown after successful creation
        dpg.add_button(label="Next", callback=next_step, show=False, tag="next_button")

        # Sub-managers: physics, actor, and source

        dpg.set_primary_window("simulation_setup_window", True)

def simulation_editor():
    with dpg.window(label="Run Simulation", width=300, height=100, pos=(50, 500)):
        dpg.add_text("Step 2", color=(0, 255, 0))
        dpg.add_button(label="Run Simulation", callback=run_simulation)
        dpg.add_text("Status:", tag="status_text", color=(255, 255, 0))

    with dpg.window(label="2. Volume Manager", width=400, height=300, pos=(600, 50)):
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
        dpg.add_text("Volume Status: ", tag="volume_status", color=(255, 255, 0))

def view():
    dpg.create_context()
    dpg.create_viewport(title="Gate wrapper", width=1050, height=650)
    dpg.setup_dearpygui()

    simulation_setup()

    dpg.show_viewport()
    dpg.start_dearpygui()   # while dpg.is_dearpygui_running(): ... dpg.render_dearpygui_frame()
    dpg.destroy_context()