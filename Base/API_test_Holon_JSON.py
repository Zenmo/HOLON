import json
import pandas as pd
from anylogiccloudclient.client.cloud_client import CloudClient
path = 'D:/Users/HOUJ/Documents/GitHub/HOLON/Base/'

client = CloudClient("f105b75c-4265-4c79-ab36-a9d6e7532fc0")

version = client.get_latest_model_version("Holon JSON")

#### Experiment 2 with other json inputs and fetch outputs 

# Create an Inputs object with the default input values
inputs = client.create_default_inputs(version)
inputs.names()

actorInputFile1 = 'config_actors.txt'
gridConnectionInputFile1 = 'config_netConnections.txt'

print(path+actorInputFile1)

with open(path+actorInputFile1,'r') as f:
    ActorInputdata1 = json.loads(f.read())
    
with open(path+gridConnectionInputFile1,'r') as f:
    gridConnectionInputdata1 = json.loads(f.read())

ActorInputdata1
gridConnectionInputdata1

inputs = client.create_default_inputs(version)
inputs.names()

inputs.set_input('P actors config JSON', ActorInputdata1)
inputs.set_input('P grid connection config JSON', gridConnectionInputdata1)

simulation = client.create_simulation(inputs)

outputs = simulation.get_outputs_and_run_if_absent()
outputs.names()
jsonOutput = outputs.value('O output JSON')

data = json.loads(jsonOutput)
df_nested_list = pd.json_normalize(data, record_path =['greatSucces'])
print(df_nested_list)
df_nested_list.to_excel(path+"outputAPI.xlsx")

#### Experiment 2 with other json inputs and fetch outputs

actorInputFile2 = 'config_actors2.txt'
gridConnectionInputFile2 = 'config_netConnections2.txt'

print(path+actorInputFile2)

with open(path+actorInputFile2,'r') as f:
    ActorInputdata2 = json.loads(f.read())
    
with open(path+gridConnectionInputFile2,'r') as f:
    gridConnectionInputdata2 = json.loads(f.read())

ActorInputdata2
gridConnectionInputdata2

inputs2 = client.create_default_inputs(version)
inputs2.names()

inputs2.set_input('P actors config JSON', ActorInputdata2)
inputs2.set_input('P grid connection config JSON', gridConnectionInputdata2)

simulation2 = client.create_simulation(inputs2)
outputs2 = simulation2.get_outputs_and_run_if_absent()
outputs2.names()
jsonOutput2 = outputs2.value('O output JSON')
errors2 = outputs2.value('O output exceptions')
print(errors2)

data2 = json.loads(jsonOutput2)
print(data2)
df_nested_list2 = pd.json_normalize(data2, record_path =['greatSucces'])
print(df_nested_list2)
df_nested_list2.to_excel(path+"outputAPI2.xlsx")