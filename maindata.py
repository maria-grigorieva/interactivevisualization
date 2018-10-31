import copy
import numpy as np
import pandas as pd
import calculationbasis
import changebasis


class VisDataSet:
    _names_of_dimensions = []
    _id_of_the_objects = []
    _used_ids = None
    _data_set_list = []
    _data_set_array = None
    __number_ready = False
    _clusters_set = []
    _saved_operations = []

    # Adds the given object to the dataset
    def add_object(self, new_object):
        return None

    # returns the object with the given ID
    def get_object_by_id(self, object_id, get_list=True):
        for i in range(len(self._data_set_list)):
            if object_id == self._id_of_the_objects[i]:
                return [self._id_of_the_objects[i],
                        copy.copy(self._data_set_list[i]),
                        copy.copy(self._clusters_set[i]) if len(
                            self._clusters_set) > i else None]
        return None

    # returns the object with the given number
    def get_object_by_number(self, object_number):
        if object_number < len(self._data_set_list):
            return [self._id_of_the_objects[object_number],
                    copy.copy(self._data_set_list[object_number]),
                    copy.copy(self._clusters_set[object_number]) if len(self._clusters_set) > object_number else None]
        else:
            return None

    def __get_calculation(self):
        if not self.__number_ready:
            # self._data_set_array = np.array(self._data_set_list, dtype=float)
            self._data_set_array = pd.DataFrame(data=self._data_set_list, index=self._id_of_the_objects,
                                                columns=self._names_of_dimensions[1:], dtype=float)
            self.__number_ready = True
        return True

    def __del_calculation(self):
        self.__number_ready = False;
        return True

    def __set_calculation(self, value):
        if value:
            self.__get_calculation()
        else:
            self.__del_calculation()
        return True

    calculation_ready = property(__get_calculation, __set_calculation, __del_calculation,
                                 "Check if the dataset is ready for calculations.")

    def apply_calculation(self, calculation, parameters, should_be_saved=False):
        if isinstance(calculation, calculationbasis.CalculationBase) and self.__number_ready:
            if should_be_saved:
                result = calculation.perform(self._data_set_array, parameters)
                self._saved_operations.append([calculation, parameters, should_be_saved, result])
                return result
            else:
                return calculation.perform(self._data_set_array, parameters)
        return None

    def apply_changes(self, changes, parameters, should_be_saved=False):
        if isinstance(changes, changebasis.ChangeBasis) and self.__number_ready:
            if should_be_saved:
                result = changes.perform(self._data_set_array, parameters)
                self._saved_operations.append([changes, parameters, should_be_saved, result])
            else:
                result = changes.perform(self._data_set_array, parameters)
            if result:
                self._data_set_list = self._data_set_array.values.tolist()
            return result
        return None

    ___add_object_visdataset = add_object
    ___get_object_by_id_visdataset = get_object_by_id
    ___get_object_by_number_visdataset = get_object_by_number


class VisDataSetWithID(VisDataSet):

    # Adds the given object to the dataset
    def add_object(self, new_object):
        if len(new_object) != len(self._names_of_dimensions) or (new_object[0] in self._used_ids):
            return False
        for i in range(1, len(new_object)):
            if not (type(new_object[i]) is float or type(new_object[i]) is int):
                return False
        self._id_of_the_objects.append(new_object[0])
        self._used_ids.add(new_object[0])
        temp_object = copy.copy(new_object)
        temp_object.remove(new_object[0])
        self._data_set_list.append(temp_object)
        self.__number_ready = False
        return True


class VisDataSetWithoutID(VisDataSet):

    # Adds the given object to the dataset
    def add_object(self, new_object):
        if len(new_object) != len(self._names_of_dimensions) - 1:
            return False
        for i in new_object:
            if not (type(i) is float or type(i) is int):
                return False
        self._id_of_the_objects.append(len(self._data_set_list))

        temp_object = copy.copy(new_object)
        self._data_set_list.append(temp_object)
        self.__number_ready = False
        return True

    def get_object_by_id(self, object_id):
        return self.get_object_by_number(object_id)


# Creates the dataset with given dimension names.
def create_dataset_with_names(dimension_names=None, has_id=True):
    if dimension_names is None:
        return None
    if has_id:
        result = VisDataSetWithID()
    else:
        result = VisDataSetWithoutID()
    result._names_of_dimensions = copy.deepcopy(dimension_names)
    if not has_id:
        result._names_of_dimensions.insert(0, "ID")
    result._id_of_the_objects = []
    result._data_set_list = []
    result._used_ids = set()
    result._max_values = []
    result._min_values = []
    result._sum_values = []

    return result


def create_dataset_without_names(dimension_count=3, has_id=True):
    if isinstance(dimension_count, int) and dimension_count > 0:
        dimension_names = ["ID"] if has_id else []
        for i in range(1, dimension_count + 1):
            dimension_names.append("X" + str(i))
        return create_dataset_with_names(dimension_names, has_id)
    else:
        return None
