import re
import time
import json

from experiments.client import Client
from .outcomes import Outcomes


class AnyLogicExperiment(Outcomes):
    def __init__(self, experiment):
        self.experiment = experiment
        self.client = Client(experiment)
        self.duration_s = 0
        self.rawData = {}

    def loadRawData(self):
        self.rawData = self.client.rawData
        #print(self.rawData)
    

    def runScenario(self, inputs):

        for anylogic_variable_key, input_value in inputs.items():

            inputs = json.loads(self.client.inputs.get_input(anylogic_variable_key))
            idx_to_update = next(
                idx
                for idx, item in enumerate(inputs)
                if item["id"] == input_value["id"]
            )
            inputs[idx_to_update] = input_value

            self.client.inputs.set_input(anylogic_variable_key, json.dumps(inputs))

        self.outcomes = self.client.run_simulation()

        return self.outcomes

    def runSimulation(self):
        """Runs a simulation and writes some outcomes"""
        startTime_ms = round(time.time() * 1000)
        print("Working...")
        outputs = self.client.run_simulation()
        endTime_ms = round(time.time() * 1000)

        print("\tAvailable outputs: \n\t\t -", "\n\t\t - ".join(outputs.names()))
        self.outcomes = outputs

        if self.experiment.log_exceptions:
            self.exceptions = outputs.value("O output exceptions")
            print("\t\033[91mReturned exceptions: ", self.exceptions, "\033[0m")

        endTimeData_ms = round(time.time() * 1000)

        self.duration_s = (endTime_ms - startTime_ms) / 1000
        totalDuration_s = (endTimeData_ms - startTime_ms) / 1000
        print("\tCloud run response time = ", self.duration_s, " s")
        print("\tCloud data response time = ", totalDuration_s, " s")

        print("\nWriting outcomes..")
        self.write_outcomes()
