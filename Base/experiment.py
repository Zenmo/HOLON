#import json
#import pandas as pd
import generateConfigJSONs as jsons

class Experiment:
    gridNodeConfigData = ''
    gridConnectionConfigData = ''
    energyAssetConfigData = ''
    actorsConfigData = ''
    policyConfigData = ''

    # constructor
    def __init__(self, path, experiment_name, model_name, experiment_configxlsx, timestep_hours, forceUnCached, progressUpdates, parallelize):
        self.path = path
        self.name = experiment_name
        self.modelName = model_name
        self.configFile = experiment_configxlsx
        self.timeStep_h = timestep_hours
        self.forceUnCached = forceUnCached
        self.progressUpdates = progressUpdates
        self.parallelize = parallelize
  
    def printSettings(self):
        print("Experiment settings: "+self.name)
        print("Path: ", self.path)
        print("Model: ", self.modelName)
        print("Config: ", self.configFile)
        print("TimeStep_h: ", self.timeStep_h)
        print("Force Uncached: ", self.forceUnCached)
        print("Show progress: ", self.progressUpdates)
        print("Paralellize: ", self.parallelize)

    def generateConfigJSONs(self):
        print("start creating json files: "+self.name)
        config_jsons = jsons.ConfigJSONs(self)
        config_jsons.generateJSONs()
        self.gridNodeConfigData = config_jsons.gridNodeConfigJSONs
        self.gridConnectionConfigData = config_jsons.gridConnectionConfigJSONs
        self.energyAssetConfigData = config_jsons.energyAssetsConfigJSONs
        self.actorsConfigData = config_jsons.actorsConfigJSONs
        self.policyConfigData = config_jsons.policyConfigJSONs

        