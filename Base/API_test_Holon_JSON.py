import json
import pandas as pd
import time

from anylogiccloudclient.client.cloud_client import CloudClient


class AnyLogicExperiment:
    # client = CloudClient("f105b75c-4265-4c79-ab36-a9d6e7532fc0")

    client = CloudClient("23cd7f85-d254-406b-b69c-66d23dfc9fd8", "http://5.9.100.203")
    version = client.get_latest_model_version("Base")
    inputs = ""
    simulation = ""
    outputs = ""
    duration_s = 0

    def __init__(self, experiment):
        self.experiment = experiment
        # self.model = model

    def setInputs(self):
        # actorInputFile1 = 'config_actors_moreAgents.txt'
        # gridConnectionInputFile1 = 'config_netConnections_moreAgents.txt'

        # Create an Inputs object with the default input values
        self.inputs = self.client.create_default_inputs(self.version)
        print(self.inputs.names())

        # print(path+actorInputFile1)

        # with open(self.experiment.path+"\\"+actorInputFile1,'r') as f:
        #    ActorInputdata1 = json.loads(f.read())

        # with open(self.experiment.path+"\\"+gridConnectionInputFile1,'r') as f:
        #    gridConnectionInputdata1 = json.loads(f.read())

        # print("**** actordata from file ***")
        # print(ActorInputdata1)
        # print("**** actordata from experiment object ****")
        # print(self.experiment.actorsConfigData)
        # self.experiment.actorsConfigData = json.loads(self.experiment.actorsConfigData)
        # self.experiment.gridConnectionConfigData = json.loads()
        # print("*** reimaginged ***")
        # print(actordata)
        # gridConnectionInputdata1

        self.inputs.set_input("P actors config JSON", self.experiment.actorsConfigData)
        self.inputs.set_input(
            "P grid connection config JSON", self.experiment.gridConnectionConfigData
        )
        self.inputs.set_input(
            "P grid node config JSON", self.experiment.gridNodeConfigData
        )
        self.inputs.set_input(
            "P energy assets config JSON", self.experiment.energyAssetConfigData
        )
        self.inputs.set_input("P time step h", self.experiment.timeStep_h)

        print("inputs set!")

    def runSimulation(self):
        startTime_ms = round(time.time() * 1000)
        print("working...")
        self.simulation = self.client.create_simulation(self.inputs)

        self.outputs = self.simulation.get_outputs_and_run_if_absent()
        print("Outputs: ", self.outputs.names())
        jsonOutput = self.outputs.value("O output JSON")
        exceptions = self.outputs.value("O output exceptions")
        print("Returned exceptions: ", exceptions)
        endTime_ms = round(time.time() * 1000)

        self.duration_s = (endTime_ms - startTime_ms) / 1000
        print("cloud response time = ", self.duration_s, " s")

        data = json.loads(jsonOutput)
        df_nested_list = pd.json_normalize(data, record_path=["greatSucces"])
        print(df_nested_list)
        df_nested_list.to_excel(
            self.experiment.path + "\\" + "outputAPI_" + self.experiment.name + ".xlsx"
        )

    #
    ##### Experiment 2 with other json inputs and fetch outputs

    # actorInputFile2 = 'config_actors2.txt'
    # gridConnectionInputFile2 = 'config_netConnections2.txt'

    # print(path+actorInputFile2)

    # with open(path+"\\"+actorInputFile2,'r') as f:
    #    ActorInputdata2 = json.loads(f.read())

    # with open(path+"\\"+gridConnectionInputFile2,'r') as f:
    #    gridConnectionInputdata2 = json.loads(f.read())

    # ActorInputdata2
    # gridConnectionInputdata2

    # inputs2 = client.create_default_inputs(version)
    # inputs2.names()

    # inputs2.set_input('P actors config JSON', ActorInputdata2)
    # inputs2.set_input('P grid connection config JSON', gridConnectionInputdata2)

    # simulation2 = client.create_simulation(inputs2)
    # outputs2 = simulation2.get_outputs_and_run_if_absent()
    # outputs2.names()
    # jsonOutput2 = outputs2.value('O output JSON')
    # errors2 = outputs2.value('O output exceptions')
    # print(errors2)

    # data2 = json.loads(jsonOutput2)
    # print(data2)
    # df_nested_list2 = pd.json_normalize(data2, record_path =['greatSucces'])
    # print(df_nested_list2)
    # df_nested_list2.to_excel(path+"\\"+"outputAPI2.xlsx")
