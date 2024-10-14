import dearpygui.dearpygui as dpg


class View:
    def __init__(self, controller):
        self.controller = controller

    def create_user_interface(self):
        dpg.create_context()
        dpg.create_viewport(title="Gate Simulation", width=900, height=600)
        dpg.setup_dearpygui()

        self.simulation_setup()

        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

    def next_step(self):
        self.controller.create_simulation()
        dpg.delete_item("simulation_setup_window")
        self.simulation_editor()
        self.controller.display_volumes()

    def simulation_setup(self):
        with dpg.window(label="Simulation Setup", tag="simulation_setup_window", width=400, height=200, pos=(50, 50)):
            dpg.add_text("Simulation Setup")
            dpg.add_input_text(label="Simulation name", tag="user_info_name", default_value="simulation")

            with dpg.group(tag="advanced_options", show=True):
                dpg.add_text("Advanced Options", color=(0, 255, 0))
                dpg.add_checkbox(label="Visualisation", tag="user_info_visu", default_value=False)

                with dpg.collapsing_header(label="GATE Verbosity"):
                    dpg.add_combo(label="Verbose level", tag="user_info_verbose_level", items=["NOTSET", "INFO", "DEBUG"], default_value="INFO")
                    dpg.add_combo(label="Running verbose level", tag="user_info_running_verbose_level", items=["0", "1", "2"], default_value="0")

                with dpg.collapsing_header(label="Random Number Generator"):
                    dpg.add_input_text(label="Random Engine", tag="user_info_random_engine", default_value="MixMaxRng")
                    dpg.add_input_text(label="Random Seed", tag="user_info_random_seed", default_value="auto")

            dpg.add_button(label="Create", callback=self.next_step)

    def simulation_editor(self):
        with dpg.window(label="Run Simulation", width=300, height=100, pos=(500, 50)):
            dpg.add_button(label="Run Simulation", callback=self.controller.run_simulation)
            dpg.add_text("Status:", tag="status_text", color=(255, 255, 0))

        with dpg.window(label="Volume Manager", width=400, height=400, pos=(50, 50)):
            dpg.add_text("Current Volumes:")
            dpg.add_listbox([], tag="volume_list", width=300, num_items=5)

            dpg.add_combo(label="Volume type", tag="volume_type", items=["Box", "Sphere"], default_value="Box")
            dpg.add_input_text(label="Volume name", tag="volume_name")
            dpg.add_combo(label="Volume material", tag="volume_material", items=["G4_WATER", "G4_AIR"],
                          default_value="G4_WATER")

            dpg.add_slider_float(label="Volume size (mm)", tag="volume_size", min_value=1.0, max_value=100.0,
                                 default_value=50.0)

            dpg.add_slider_float(label="Position X", tag="volume_position_x", min_value=-100.0, max_value=100.0,
                                 default_value=0.0)
            dpg.add_slider_float(label="Position Y", tag="volume_position_y", min_value=-100.0, max_value=100.0,
                                 default_value=0.0)
            dpg.add_slider_float(label="Position Z", tag="volume_position_z", min_value=-100.0, max_value=100.0,
                                 default_value=0.0)

            dpg.add_button(label="Create Volume")
            dpg.add_text("Volume Status: ", tag="volume_status", color=(255, 255, 0))

    def get_value(self, tag):
        return dpg.get_value(tag)

    def update_volume_list(self, volumes):
        dpg.configure_item("volume_list", items=volumes)

