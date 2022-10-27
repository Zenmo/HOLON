from anylogiccloudclient.client.cloud_client import CloudClient
from experiments.config import config
from .inputs import Inputs


class Client(Inputs):
    def __init__(self, experiment):
        self.client = CloudClient(
            config["anylogic_cloud"]["api_key"], config["anylogic_cloud"]["url"]
        )
        self.experiment = experiment
        self.inputs = experiment.model_name

    def run_simulation(self, polling_period=10):
        """Returns the runs outputs TODO: polling period is hardcoded"""
        return self.client.create_simulation(self.inputs).get_outputs_and_run_if_absent(
            polling_period=polling_period
        )
