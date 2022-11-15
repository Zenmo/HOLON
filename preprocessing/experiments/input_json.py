import json
import pandas as pd


class InputJSON:
    def __init__(self, name, path, sheet_name, file_name):
        self.write_to_path = path / f"{name}_{sheet_name}.txt"
        self.dataRaw  = pd.read_excel(path / file_name, sheet_name=sheet_name)
        self.data = pd.read_excel(path / file_name, sheet_name=sheet_name).to_json(
            orient="records"
        )
        #print("InputJSON read jsons")
        print(self.data)

    def as_json(self, write_result=True):
        if write_result:
            self._write()
            #print("as_json wrote jsons")
        return json.loads(self.data)

    def _write(self, formatted: bool = True):
        #print("_write triggered!")
        with open(self.write_to_path, "w") as outfile:
            if formatted:
                outfile.write(json.dumps(json.loads(self.data), indent=2))
                #print("_write jsons exported")
            else:
                outfile.writelines([self.data])
                #print("_write jsons exported unformatted")
