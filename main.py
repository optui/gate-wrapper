import opengate as gate
import dearpygui.dearpygui as dpg


def main():
    # Setup DearPyGui Window
    dpg.create_context()
    # Gate simulation window
    with dpg.window(label="Gate Simulation", tag="gate_control_window", height=500, width=700):
        dpg.add_text("Welcome to gate-wrapper!")
        # Verbose Level (essential setting)
        dpg.add_combo(items=["NONE", "INFO", "DEBUG"], default_value="INFO", label="Verbose Level", tag='verbose_level')
        # Random Engine and Seed (common requirement)
        dpg.add_combo(label="Random Engine", items=["MixMaxRng", "MersenneTwister"], default_value="MersenneTwister", tag='random_engine_combo')
        dpg.add_input_text(label="Random Seed", default_value="auto", tag='random_seed')
        # Multithreading (if your simulation benefits from multiple threads)
        dpg.add_input_int(label="Number of Threads", default_value=1, min_value=1, max_value=4, tag='threads_input')
        # Visualization settings
        dpg.add_checkbox(label="Enable Visualization", tag='visu_checkbox')
        dpg.add_input_text(label="Visualization Output Filename", default_value="./output.vrml", tag='visu_filename')
        # Button to start simulation
        dpg.add_button(label="Start Simulation", callback=run_simulation)
        # Status text
        dpg.add_text("Status: Ready", tag="status_text")

    with dpg.window(label="Volume manager", tag="volumes_window", height=300, width=300):
        dpg.add_combo(label="Volumes", tag="volumes_combo")

    dpg.set_item_pos("volumes_window", [50, 50])
    dpg.set_item_pos("gate_control_window", [400, 50])

    dpg.create_viewport(title='Simulation Viewer', width=1150, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


def run_simulation():
    # Get user-defined values from DearPyGui
    verbose_level: str = dpg.get_value('verbose_level')
    random_engine = dpg.get_value('random_engine_combo')
    random_seed =   dpg.get_value('random_seed')
    num_threads = dpg.get_value('threads_input')
    visu_enabled = dpg.get_value('visu_checkbox')
    visu_filename = dpg.get_value('visu_filename')

    # Setup simulation with user-defined parameters
    sim = gate.Simulation()
    sim.verbose_level = verbose_level
    sim.random_engine = random_engine
    sim.number_of_threads = num_threads
    if random_seed != "auto": sim.random_seed = int(random_seed)
    sim.visu = visu_enabled
    if visu_enabled: sim.visu_filename = visu_filename

    # Start the simulation
    try:
        print("Running OpenGate Simulation...")
        sim.run()
        dpg.set_value("status_text", "Simulation Complete!")
    except Exception as e:
        print(f"Simulation failed: {str(e)}")
        dpg.set_value("status_text", f"Simulation Error: {str(e)}")


if __name__ == "__main__":
    main()
