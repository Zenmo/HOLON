import time

from experiments.client import Client
from .outcomes import Outcomes

class AnyLogicExperiment(Outcomes):

    def __init__(self, experiment):
        self.experiment = experiment
        self.client = Client(experiment)
        self.duration_s = 0

    def runSimulation(self):
        '''Runs a simulation and writes some outcomes'''
        startTime_ms = round(time.time() * 1000)
        print("Working...")
        outputs = self.client.run_simulation()
        endTime_ms = round(time.time() * 1000)

        print("\tAvailable outputs: ", outputs.names())
        self.outcomes = outputs

        if self.experiment.log_exceptions:
            self.exceptions = outputs.value("O output exceptions")
            print("\t\033[91mReturned exceptions: ", self.exceptions, '\033[0m')

        endTimeData_ms = round(time.time() * 1000)

        self.duration_s = (endTime_ms - startTime_ms) / 1000
        totalDuration_s = (endTimeData_ms - startTime_ms) / 1000
        print("\tCloud run response time = ", self.duration_s, " s")
        print("\tCloud data response time = ", totalDuration_s, " s")

        print('\nWriting outcomes..')
        self.write_outcomes()
