from anylogiccloudclient.client.cloud_error import CloudError


class Inputs:
    @property
    def inputs(self):
        return self._inputs

    @inputs.setter
    def inputs(self, model_name):
        self._inputs = self.client.create_default_inputs(self._version(model_name))
        self._set_config_sheets()
        self._set_extras()
        self._set_local()

    def _version(self, model_name):
        try:
            return self.client.get_latest_model_version(model_name)
        except CloudError as e:
            raise KeyError(
                f"Could not retrieve the model you specified for this model_name: '{model_name}'."
                + f" Please check whether the model is shared (as dev) with you at {self.client.host_url}."
                + f" Caught CloudError: {e}"
            )

    def _set_config_sheets(self):
        for input in self.experiment.inputs:
            self._set_config_sheet(input["anylogic_key"], input["file"])

    def _set_config_sheet(self, input_name, config_sheet):
        try:
            self._inputs.set_input(
                input_name, self.experiment.config_json_for(config_sheet)
            )
        except StopIteration:
            raise KeyError(f"Input {input_name} is unkown to the model")

    def _set_extras(self):
        try:
            for input_name, value in self.experiment.extra_settings():
                self._inputs.set_input(input_name, value)
        except:
            pass

    def _set_local(self):
        try:
            self._inputs.set_input("P import local config jsons", False)
        except:
            print("\033[93mVariable P import local config jsons not available\033[0m\n")
