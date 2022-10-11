import pandas as pd
import json

class ConfigJSONs:
    gridNodeConfigJSONs = ''
    gridConnectionConfigJSONs = ''
    energyAssetsConfigJSONs = ''
    actorsConfigJSONs = ''
    policyConfigJSONs = ''

    # constructor
    def __init__(self, experiment):
        self.experiment = experiment
    
    def loadDataFromExcelSheet(self, sheet):
        excel_data_df = pd.read_excel(self.experiment.path+'\\'+self.experiment.configFile, sheet_name=sheet)
        return excel_data_df

    def convertExcelToJson(self, excelsheet):
        json_str = excelsheet.to_json(orient='records')
        print(json_str)
        return json_str

    def jsonForJava(self, json_string):
        #json_string = json.dumps(json_string, cls=EnhancedJSONEncoder)
        #json_string = json_string.replace('"', r"\"")
        #json_string = '"' + json_string + '"'
        print(json_string)
        return json_string
        
    def outputJSONfile(self, json_string,sheet):
        with open(self.experiment.path+'\\'+sheet+"_"+self.experiment.name+".txt", "w") as outfile:
            outfile.writelines([json_string])

    def processExcelSheet(self, sheet):
        exceldata = self.loadDataFromExcelSheet(sheet)
        json_str = self.convertExcelToJson(exceldata)
        json_str = self.jsonForJava(json_str)
        self.outputJSONfile(json_str, sheet)
        json_str = json.loads(json_str)
        return json_str

    def generateJSONs(self):
        self.gridNodeConfigJSONs = self.processExcelSheet('config_gridNodes')
        self.gridConnectionConfigJSONs = self.processExcelSheet('config_gridConnections')
        self.energyAssetsConfigJSONs = self.processExcelSheet('config_energyAssets')
        self.actorsConfigJSONs = self.processExcelSheet('config_actors')
        self.policyConfigJSONs = self.processExcelSheet('config_policies')


    #if __name__ == "__main__":
    #   main()