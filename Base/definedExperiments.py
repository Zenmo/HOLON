import pathlib
import experiment as exp
import API_test_Holon_JSON as api

path = str(pathlib.Path(__file__).parent.resolve())

#Experiment default
experiment_default = exp.Experiment(path, "default", "db_backboneConfig.xlsx", 1)
experiment_default.printSettings()
experiment_default.generateConfigJSONs()

# Run experiment in AnyLogic Cloud
api_experiment_default = api.AnyLogicExperiment(experiment_default)
api_experiment_default.setInputs()
api_experiment_default.runSimulation()
print("duration: ", api_experiment_default.duration_s, " seconds")

##
#Experiment with more agents
experiment_moreAgents = exp.Experiment(path, "moreAgents", "db_backboneConfig_moreagents.xlsx", 1)
experiment_moreAgents.printSettings()
experiment_moreAgents.generateConfigJSONs()

# Run experiment in AnyLogic Cloud
api_experiment_moreAgents = api.AnyLogicExperiment(experiment_moreAgents)
api_experiment_moreAgents.setInputs()
api_experiment_moreAgents.runSimulation()
print("duration: ", api_experiment_moreAgents.duration_s, " seconds")




