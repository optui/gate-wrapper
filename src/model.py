from pathlib import Path

import opengate as gate
from opengate.utility import read_mac_file_to_commands, g4_units


class SimulationModel:
    def __init__(self, **kwargs):
        user_info = {
            "name":'simulation',
            "verbose_level":'INFO',  # Gate pre-run verbosity. NOTSET=0, DEBUG=10, INFO=20
            "verbose_close":False,  # Switch on/off verbose output in close() methods.
            "verbose_getstate":False,  # Switch on/off verbose output in __getstate__() methods.
            "running_verbose_level":0,  # Gate verbosity during running.
            "g4_verbose_level":1,  # Geant4 verbosity.
            "g4_verbose":False,  # Switch on/off Geant4's verbose output.
            "g4_verbose_level_tracking":-1, # Activate verbose tracking in Geant4 via G4 command '/tracking/verbose g4_verbose_level_tracking'.
            "visu":False,  # Activate visualization? Note: Use low number of primaries if you activate visualization.
            "visu_type":'vrml', # The type of visualization to be used. qt, vrml, gdml,vrml_file_only, gdml_file_only
            "visu_filename":None, # Name of the file where visualization output is stored. Only applicable for vrml and gdml. Type: Path
            "visu_verbose":False,  # Should verbose output be generated regarding the visualization?
            "visu_commands":read_mac_file_to_commands("default_visu_commands_qt.mac"), # Geant4 commands needed to handle the visualization.
            "visu_commands_vrml":read_mac_file_to_commands("default_visu_commands_vrml.mac"), # Geant4 commands needed to handle the VRML visualization.
            "visu_commands_gdml":read_mac_file_to_commands("default_visu_commands_gdml.mac"), # Geant4 commands needed to handle the GDML visualization.
            "check_volumes_overlap":True, # If true, Gate will also check whether volumes overlap. Note: Geant4 checks overlaps in any case.
            "number_of_threads":1, # Number of threads on which the simulation will run. Geant4's run manager will run in MT mode if more than 1 thread is requested. Requires Geant4 do be compiled with Multithread flag TRUE.
            "force_multithread_mode":False,  # Force Geant4 to run multihthreaded even if 'number_of_threads' = 1.
            "random_engine":'MixMaxRng',  # Name of the Geant4 random engine to be used.
            "random_seed":'auto', # Random seed to be used by the random engine. Setting a specific value will make subsequent simulation runs to produce identical results.
            "run_timing_intervals":[[0 * g4_units.second, 1 * g4_units.second]], # A list of timing intervals provided as 2-element lists of begin and end values
            "output_dir":'.', # Directory to which any output is written, unless an absolute path is provided for a specific output.
            "store_json_archive":False, # Automatically store a json file containing all parameters of the simulation after the run?
            "json_archive_filename":Path("simulation.json"), # Name of the json file containing all parameters of the simulation. It will be saved in the location specified via the parameter 'output_dir'. Default filename: simulation.json
            "store_input_files":False,  # Store all input files used in the simulation? Default: False
            "g4_commands_before_init":[], # Geant4 commands which will be called before the G4 runmanager has initialized the simulation. required_type: str
            "g4_commands_after_init":[], # Geant4 commands which will be called after the G4 runmanager has initialized the simulation. required_type: str
            "init_only":False,  # Start G4 engine initialisation but do not start the simulation.
            "progress_bar":False  # Display a progress bar during the simulation
        }

        user_info.update(kwargs)

        self.simulation = gate.Simulation(**user_info)

        self.volume_model: VolumeModel = VolumeModel(self.simulation.volume_manager)
        self.source_model = SourceModel(self.simulation.source_manager)
        self.actor_model = ActorModel(self.simulation.actor_manager)
        self.physics_model = PhysicsModel(self.simulation.physics_manager)

    def run(self):
        self.simulation.run(True)

class VolumeModel:
    def __init__(self, volume_manager):
        self.volume_manager: gate.managers.VolumeManager = volume_manager

    def get_volumes(self):
        return list(self.volume_manager.volumes.keys())

class SourceModel:
    def __init__(self, source_manager):
        self.source_manager = source_manager


class ActorModel:
    def __init__(self, actor_manager):
        self.actor_manager = actor_manager


class PhysicsModel:
    def __init__(self, physics_manager):
        self.physics_manager = physics_manager

class FilterModel:
    def __init__(self, filter_manager):
        self.filter_manager = filter_manager