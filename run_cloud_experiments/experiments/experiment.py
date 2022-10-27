import random
from dataclasses import dataclass, field
from pathlib import Path
from .input_json import InputJSON

@dataclass
class Experiment:
    name: str
    path: Path
    model_name: str
    config_file: str
    timestep_hours: float = 0.25
    force_uncached: bool = True
    show_progress: bool = False
    parallelize: bool = True
    log_exceptions: bool = False
    outcomes: list = field(default_factory=list)
    inputs: list = field(default_factory=list)

    def __repr__(self):
        return (f"\n\033[4mExperiment {self.name}\033[0m\n" +
            f"Path: {self.path}\n" +
            f"Model: {self.model_name}\n" +
            f"Config: {self.config_file}\n" +
            f"TimeStep_h: {self.timestep_hours}\n"+
            f"Force Uncached: {self.force_uncached}\n" +
            f"Show progress: {self.show_progress}\n" +
            f"Paralellize: {self.parallelize}\n\033[0m")

    def extra_settings(self):
        '''TODO: move this to config'''
        if self.force_uncached:
            yield "P force uncached", random.random()
        if self.parallelize:
            yield "P parallelize", self.parallelize
        yield "P import local config jsons", False

    def config_json_for(self, sheet_name):
        '''Returns a JSON containing the config information'''
        return InputJSON(self.name, self.path, sheet_name, self.config_file).as_json()
