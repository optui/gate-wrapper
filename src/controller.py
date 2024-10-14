from model import SimulationModel
from view import View


class SimulationController:
    def __init__(self):
        self.view = View(self)
        self.simulation_model = None

    def create_simulation(self):
        name = self.view.get_value("user_info_name")
        visu = self.view.get_value("user_info_visu")
        verbose_level = self.view.get_value("user_info_verbose_level")
        running_verbose_level = int(self.view.get_value("user_info_running_verbose_level"))
        random_engine = self.view.get_value("user_info_random_engine")
        random_seed = self.view.get_value("user_info_random_seed")

        self.simulation_model = SimulationModel(
            name=name,
            visu=visu,
            verbose_level=verbose_level,
            running_verbose_level=running_verbose_level,
            random_engine=random_engine,
            random_seed=random_seed
        )

    def display_volumes(self):
        volumes = self.simulation_model.volume_model.get_volumes()
        print(volumes)
        self.view.update_volume_list(volumes)

    def run_simulation(self):
        self.simulation_model.run()
