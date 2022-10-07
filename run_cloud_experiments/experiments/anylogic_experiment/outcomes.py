import json
import pandas as pd

class Outcomes():
    @property
    def outcomes(self):
        return self._outcomes

    @outcomes.setter
    def outcomes(self, outputs):
        self._outcomes = {
            outcome['human_key'] : self._calc_value(outputs, outcome)
            for outcome in self.experiment.outcomes
        }

    def write_outcomes(self):
        for outcome in self.experiment.outcomes:
            if outcome['write']:
                self._write_outcome(outcome)
            if outcome['print']:
                print(self.outcomes[outcome['human_key']])

    def _write_outcome(self, outcome):
        self.outcomes[outcome['human_key']].to_excel(
            self._output_folder() / f"{outcome['human_key']}_{self.experiment.name}.xlsx"
        )

    def _output_folder(self):
        path = self.experiment.path / 'output' / self.experiment.name
        path.mkdir(exist_ok=True, parents=True)
        return path

    def _calc_value(self, outputs, outcome):
        raw_data = json.loads(outputs.value(outcome['anylogic_key']))

        # Some special cases to make json_normalize accept the object
        if isinstance(raw_data, list) and isinstance(raw_data[0], float):
            raw_data =  [{outcome['human_key']: raw_value} for raw_value in raw_data]
        elif isinstance(raw_data, float):
            raw_data = {outcome['human_key']: raw_data}

        value = pd.json_normalize(raw_data)

        if outcome.get('action', '') == 'normalise':
            return value / value.sum()

        return value
