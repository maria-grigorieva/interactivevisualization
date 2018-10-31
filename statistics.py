import calculationbasis
import pandas as pd


class BasicStatistics(calculationbasis.CalculationBase):

    def perform(self, data, parameters):
        if isinstance(data, pd.DataFrame):
            max = data.max()
            min = data.min()
            sum = data.sum()
            avg = data.sum() / data.shape[0]
            mean = data.mean()
            std = data.std()
            return [max, min, sum, avg, mean, std]

        return None
