#import json
#import pandas as pd
import generateConfigJSONs as jsons

class Experiment:
    gridNodeConfigData = ''
    gridConnectionConfigData = ''
    energyAssetConfigData = ''
    actorsConfigData = ''

    # constructor
    def __init__(self, path, experiment_name, model_name, experiment_configxlsx, timestep_hours, forceUnCached, progressUpdates):
        self.path = path
        self.name = experiment_name
        self.modelName = model_name
        self.configFile = experiment_configxlsx
        self.timeStep_h = timestep_hours
        self.forceUnCached = forceUnCached
        self.progressUpdates = progressUpdates
  

    def printSettings(self):
        print("Experiment settings: "+self.name)
        print(self.path)
        print(self.modelName)
        print(self.configFile)
        print(self.timeStep_h)
        print(self.progressUpdates)

    def generateConfigJSONs(self):
        print("start creating json files: "+self.name)
        config_jsons = jsons.ConfigJSONs(self)
        config_jsons.generateJSONs()
        self.gridNodeConfigData = config_jsons.gridNodeConfigJSONs
        self.gridConnectionConfigData = config_jsons.gridConnectionConfigJSONs
        self.energyAssetConfigData = config_jsons.energyAssetsConfigJSONs
        self.actorsConfigData = config_jsons.actorsConfigJSONs

        