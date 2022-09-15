import json
import pandas as pd
import pathlib

path = str(pathlib.Path(__file__).parent.resolve())

filename = 'output-2.json'
print(path+"\\"+filename)

with open(path+"/"+filename,'r') as f:
    data = json.loads(f.read())

print(data)
df_nested_list = pd.json_normalize(data, record_path =['greatSucces'])

#json_str = pd.read_json(path+'/'+filename,orient='values')
print(df_nested_list)

df_nested_list.to_excel(path+'/'+"output.xlsx")