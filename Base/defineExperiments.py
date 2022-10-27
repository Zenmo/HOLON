import pathlib
import experiment as exp
import API_test_Holon_JSON as api

path = str(pathlib.Path(__file__).parent.resolve())

forceUncached = True
showProgress = False
parallelize = False

##
# #Experiment default
experiment_default = exp.Experiment(
    path,
    "default",
    "BaseParTest",
    # "BaseParallel",
    "db_backboneConfig.xlsx",
    1,
     forceUncached,
     showProgress,
     parallelize,
 )
experiment_default.printSettings()
experiment_default.generateConfigJSONs()
experiment_default.actorsConfigData

# # Run experiment in AnyLogic Cloud
# api_experiment_default = api.AnyLogicExperiment(experiment_default)
# api_experiment_default.setInputs()
# api_experiment_default.runSimulation()
# # print("duration: ", api_experiment_default.duration_s, " seconds")
# print("***** runSettings *******" + api_experiment_default.OutputRunSettings)

##
# #Experiment with 300 agents
experiment_300 = exp.Experiment(
    path,
    "300_gridConnections",
    "BaseParTest",
    "db_backboneConfig_300.xlsx",
    0.25,
    forceUncached,
    showProgress,
    parallelize,
)
experiment_300.printSettings()
experiment_300.generateConfigJSONs()
experiment_300.actorsConfigData

# Run experiment in AnyLogic Cloud
api_experiment_300 = api.AnyLogicExperiment(experiment_300)
api_experiment_300.setInputs()
api_experiment_300.runSimulation()
# api_experiment_300.checkProgress()
print("duration: ", api_experiment_300.duration_s, " seconds")
print("***** runSettings *******" + api_experiment_300.OutputRunSettings)

# # Experiment with 1000 agents
# experiment_1000 = exp.Experiment(
#     path,
#     "1000_gridConnections",
#     "BaseParTest",
#     # "BaseParallel",
#     "db_backboneConfig_1000.xlsx",
#     1,
#     forceUncached,
#     showProgress,
#     parallelize,
# )
# experiment_1000.printSettings()
# experiment_1000.generateConfigJSONs()
# experiment_1000.actorsConfigData

# # Run experiment in AnyLogic Cloud
# api_experiment_1000 = api.AnyLogicExperiment(experiment_1000)
# api_experiment_1000.setInputs()
# api_experiment_1000.runSimulation()
# # print("***** AgentData received *****"+api_experiment_1000.OutputAgentData)
# print("duration: ", api_experiment_1000.duration_s, " seconds")
# print("***** runSettings *******" + api_experiment_1000.OutputRunSettings)
