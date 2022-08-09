from .with_two_values import WithTwoValuesConverter

class Multiply(WithTwoValuesConverter):
    def calculate(self):
        '''Calculates and updates the main_value'''
        if not self.main_value.is_set():
            return

        self.main_value.multiply(self.second_value)
