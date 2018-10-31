import calculationbasis
import pandas as pd


class BasicNumbersCalculation(calculationbasis.CalculationBase):

    def perform(self, data, parameters):
        if isinstance(data, pd.DataFrame):
            resultmax = data.max()
            resultmin = data.min()
            resultsum = data.sum()
            resultavg = data.sum() / data.shape[0]
            return [resultmax, resultmin, resultsum, resultavg]

        return None
