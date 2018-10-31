import pandas as pd
import changebasis


class NormalizeData(changebasis.ChangeBasis):
    def perform(self, data, parameters):
        if not isinstance(data, pd.DataFrame):
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
        min_in_data = data.min()
        dif_in_data = data.max() - min_in_data
        multiplier = max_value
        for i in range(len(max_value)):
            multiplier[i] -= min_value[i]

        for i in data.index:
            data.loc[i] = (data.loc[i] - min_in_data) / dif_in_data * multiplier + min_value
        # while not iterator.finished:
        #     iterator[0] = (iterator[0] - min_in_data[iterator.multi_index[1]]) / \
        #                   (dif_in_data[iterator.multi_index[1]]) * multiplier[iterator.multi_index[1]] + \
        #                   min_value[iterator.multi_index[1]]
        #     iterator.iternext()
        return True
