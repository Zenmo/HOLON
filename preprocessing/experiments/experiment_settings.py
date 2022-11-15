import yaml
from pathlib import Path

TOP_FOLDER = Path(__file__).parent


class ExperimentSettings:
    def __init__(self, experiments):
        self.experiments = experiments

    def all(self):
        """Returns a Generator of experiments"""
        return (self.get(name, settings) for name, settings in self.experiments.items())

    def get(self, name, settings):
        return ExperimentSetting(name, settings).setting

    def find(self, experiment_name):
        """
        Returns settings for the expermient with that name,
        return blank settings if it doesn't exist
        """
        self.experiments.get(experiment_name, self.get(experiment_name, {}))

    @classmethod
    def load(cls, path="config/experiments.yml"):
        path = TOP_FOLDER.parent / path
        with open(path, "r") as f:
            doc = yaml.load(f, Loader=yaml.FullLoader)
        return cls(doc)


class ExperimentSetting:
    def __init__(self, name, settings):
        settings["name"] = name
        self.setting = settings

    @property
    def setting(self):
        return self._setting

    @setting.setter
    def setting(self, settings):
        self._setting = settings
        self._setting["path"] = (TOP_FOLDER / settings.get("path")).resolve()
