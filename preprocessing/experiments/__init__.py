import pandas as pd

from .anylogic_experiment import AnyLogicExperiment
from .experiment_settings import ExperimentSettings
from .experiment import Experiment
from .validate import validate_inputs
from .preprocess import generate_energyassets

"""TODO: install pandas and check if everything works!"""


def run_all():
    """Runs all experiments"""
    experiments = ExperimentSettings.load()
    for experiment_setting in experiments.all():
        start_experiment(experiment_setting)


def run_one(experiment_name):
    experiments = ExperimentSettings.load()
    start_experiment(experiments.find(experiment_name))


def run_one_scenario(experiment_name, inputs):

    experiments = ExperimentSettings.load()
    settings = experiments.get(
        experiment_name, experiments.experiments[experiment_name]
    )

    experiment = Experiment(**settings)

    # Run experiment in AnyLogic Cloud
    api_experiment = AnyLogicExperiment(experiment)
    outcome = api_experiment.runScenario(inputs)
    
    return outcome


def start_experiment(settings):
    """Runs one experiments"""
    experiment = Experiment(**settings)
    print("experiment started")
        
    # Run experiment in AnyLogic Cloud
    api_experiment = AnyLogicExperiment(experiment)
    #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    api_experiment.loadRawData()

    # Test for validation of inputs
    if experiment.validate_input:
        validate_inputs.validateInputs(api_experiment)
    
    # Test for auto-generation of energyassets:
    slider_buildingPV_kWp = 1  # test value
    slider_solarPanels_MWp = 1
    slider_gridBatteryCapacity_MWh = 1
    slider_heatpumps = 0

    # Generate corresponding assets for buildings and solar farm
    if experiment.generate_energyassets:
        api_experiment = generate_energyassets.changeExistingAssets(api_experiment, slider_buildingPV_kWp, "Building_solarpanels_", f'Building_solarpanels_{slider_buildingPV_kWp}kWp')
        api_experiment = generate_energyassets.changeExistingAssets(api_experiment, slider_solarPanels_MWp, "Solarpanels_", f'Solarpanels_{slider_solarPanels_MWp}MW')
        api_experiment = generate_energyassets.changeExistingAssets(api_experiment, slider_gridBatteryCapacity_MWh, "Grid_battery_", f'Grid_battery_{slider_gridBatteryCapacity_MWh}MWh')
        if slider_heatpumps == 1:
            api_experiment = generate_energyassets.changeToDifferentAsset(api_experiment, 'Building_gas_burner_60kW', 'Building_heatpump_20kW' )
        
                

        api_experiment.experiment.reconfig_json_for('config_energyAssets', api_experiment.rawData)
           
    if experiment.query_api:
        api_experiment.runSimulation()

        print("\nDuration: ", api_experiment.duration_s, " seconds\n")
