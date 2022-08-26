from xml.etree.ElementTree import tostring
import pandas

import pandas as pd
import openpyxl, pprint, json
import excel2json
import pathlib
path = str(pathlib.Path(__file__).parent.resolve())

file = 'db_backboneConfig.xlsx'

def loadDataFromExcelSheet(path, file, sheet):
    excel_data_df = pd.read_excel(path+'/'+file, sheet_name=sheet)
    return excel_data_df


def convertExcelToJson(excelsheet):
    json_str = excelsheet.to_json(orient='records')
    print(json_str)
    return json_str

def jsonForJava(json_string):
    #str = json.dumps(output, cls=EnhancedJSONEncoder)
    json_string = json_string.replace('"', r"\"")
    json_string = '"' + json_string + '"'
    print(json_string)
    return json_string
    
def outputJSONfile(json_string,sheet):
    with open(path+'/'+sheet+".json", "w") as outfile:
        outfile.writelines([json_string])

def processExcelSheet(sheet):
    exceldata = loadDataFromExcelSheet(path, file, sheet)
    json_str = convertExcelToJson(exceldata)
    json_str = jsonForJava(json_str)
    outputJSONfile(json_str, sheet)

def main():
    processExcelSheet('config_netNodes')
    processExcelSheet('config_netConnections')
    processExcelSheet('config_actors')
    processExcelSheet('config_energyAssets')
    
if __name__ == "__main__":
    main()