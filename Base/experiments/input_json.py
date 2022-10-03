import json
import pandas as pd

class InputJSON():
    def __init__(self, name, path, sheet_name, file_name):
        self.write_to_path = path / f"{sheet_name}_{name}.txt"
        self.data = pd.read_excel(path / file_name, sheet_name=sheet_name).to_json(orient='records')

    def as_json(self, write_result=False):
        if write_result:
            self._write()
        return json.loads(self.data)

    def _write(self):
        with open(self.write_to_path, "w") as outfile:
            outfile.writelines([self.data])
