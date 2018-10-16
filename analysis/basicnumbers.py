import analysis.calculationbasis
import numpy as np


class BasicNumbersCalculation(analysis.calculationbasis.CalculationBase):

    def perform(self, data, parameters):
        resultmax = data.max(0)
        resultmin = data.min(0)
        resultsum = data.sum(0)
        resultavg = data.sum(0) / data.shape[0]
        return [resultmax, resultmin, resultsum, resultavg]
