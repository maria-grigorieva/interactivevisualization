import numpy as np
import analysis.changebasis


class NormalizeData(analysis.changebasis.ChangeBasis):
    def perform(self, data, parameters):
        if not isinstance(data, np.ndarray):
            return False
        if len(parameters) >= 2:
            max_value = parameters[1]
            min_value = parameters[0]
        else:
            if len(parameters) == 1:
                max_value = parameters[0]
                min_value = [0] * len(data[0])
            else:
                min_value = [0] * len(data[0])
                max_value = [1] * len(data[0])
        if (len(max_value) != data.shape[1]):
            return False
        if (len(min_value) != data.shape[1]):
            return False
        min_in_data = np.min(data, 0)
        dif_in_data = np.max(data, 0) - min_in_data
        min_value = np.array(min_value)
        multiplier = np.array(max_value) - min_value
        iterator = np.nditer(data, op_flags=['readwrite'], flags=['multi_index'])
        while not iterator.finished:
            iterator[0] = (iterator[0] - min_in_data[iterator.multi_index[1]]) / \
                          (dif_in_data[iterator.multi_index[1]]) * multiplier[iterator.multi_index[1]] + \
                          min_value[iterator.multi_index[1]]
            iterator.iternext()
        return True
