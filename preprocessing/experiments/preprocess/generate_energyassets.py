import re

def changeExistingAssets(experiment, slider_value, targetAssetName, targetAssetDefinition):
    #print("slider setting ", slider_value)

    #print(experiment.rawData['config_energyAssets'])
    
    # Werkwijze: slider = absolute waarde in energyAsset-naam


    newValue = targetAssetDefinition
    print(f"new value = {newValue}")
    #print("targetAssetName = "+f'{targetAssetName}$')
    
    #p = re.compile(targetAssetName+'*')
    #print(p.sub(targetAssetDefinition, experiment.rawData['config_energyAssets']["type2"]))
    #l = experiment.rawData['config_energyAssets']["type2"]
    #filter((lambda x: re.sub(r'Building_solarpanels_$', 'truess')),l)
    
    #experiment.rawData['config_energyAssets']["type2"] = experiment.rawData['config_energyAssets']["type2"].str.replace(f'{targetAssetName}*', newValue)      
    experiment.rawData['config_energyAssets']["type2"] = experiment.rawData['config_energyAssets']["type2"].apply(lambda x: x if targetAssetName not in x else targetAssetDefinition)
    
    print(experiment.rawData['config_energyAssets'])
    return experiment

def changeToDifferentAsset(experiment, assetToChangeKey, newAssetKey):
    targetAssetName = assetToChangeKey
    targetAssetDefinition = newAssetKey
    print(f'changing {assetToChangeKey} assets to {newAssetKey} assets..')
    experiment.rawData['config_energyAssets']["type2"] = experiment.rawData['config_energyAssets']["type2"].apply(lambda x: x if targetAssetName not in x else targetAssetDefinition)
    print(experiment.rawData['config_energyAssets'])
    return experiment
    