from .base import BaseConverter

class WithTwoValuesConverter(BaseConverter):
    def __init__(self, main_value, second_value):
        self.main_value = main_value
        self.second_value = second_value

    def required_for_calculation(self):
        '''Generator, returns all Values that should be arequested from the ETM'''
        yield self.main_value
        yield self.second_value
