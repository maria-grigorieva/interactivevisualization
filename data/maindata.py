import copy


class VisDataSet:
    _names_of_dimensions = []
    _id_of_the_objects = []
    _used_ids = None
    _data_set = []
    _clusters_set = []
    _max_values = []
    _min_values = []
    _sum_values = []

    # Adds the given object to the dataset
    def add_object(self, new_object):
        return None

    # returns the object with the given ID
    def get_object_by_id(self, object_id):
        for i in range(len(self._data_set)):
            if object_id == self._id_of_the_objects[i]:
                return [self._id_of_the_objects[i],
                        copy.copy(self._data_set[i]),
                        copy.copy(self._clusters_set[i]) if len(
                            self._clusters_set) > i else None]
        return None

    # returns the object with the given number
    def get_object_by_number(self, object_number):
        if object_number < len(self._data_set):
            return [self._id_of_the_objects[object_number],
                    copy.copy(self._data_set[object_number]),
                    copy.copy(self._clusters_set[object_number]) if len(self._clusters_set) > object_number else None]
        else:
            return None

    ___add_object_visdataset = add_object
    ___get_object_by_id_visdataset = get_object_by_id
    ___get_object_by_number_visdataset = get_object_by_number


class VisDataSetWithID (VisDataSet):

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
        self._data_set.append(temp_object)

        if 1 == len(self._data_set):
            self._sum_values = copy.copy(temp_object)
            self._max_values = copy.copy(temp_object)
            self._min_values = copy.copy(temp_object)
            return True

        if len(temp_object) != len(self._sum_values):
            self._sum_values = [0] * len(temp_object)
        if len(temp_object) != len(self._max_values):
            self._max_values = copy.copy(temp_object)
        if len(temp_object) != len(self._min_values):
            self._min_values = copy.copy(temp_object)

        for i in range(len(temp_object)):
            self._sum_values[i] += temp_object[i]
            if temp_object[i] > self._max_values[i]:
                self._max_values[i] = temp_object[i]
            if temp_object[i] < self._min_values[i]:
                self._min_values[i] = temp_object[i]
        return True


class VisDataSetWithoutID (VisDataSet):

    # Adds the given object to the dataset
    def add_object(self, new_object):
        if len(new_object) != len(self._names_of_dimensions):
            return False
        for i in new_object:
            if not (type(i) is float or type(i) is int):
                return False
        self._id_of_the_objects.append(len(self._data_set))

        temp_object = copy.copy(new_object)
        self._data_set.append(temp_object)

        if 1 == len(self._data_set):
            self._sum_values = copy.copy(temp_object)
            self._max_values = copy.copy(temp_object)
            self._min_values = copy.copy(temp_object)
            return True

        if len(temp_object) != len(self._sum_values):
            self._sum_values = [0] * len(temp_object)
        if len(temp_object) != len(self._max_values):
            self._max_values = copy.copy(temp_object)
        if len(temp_object) != len(self._min_values):
            self._min_values = copy.copy(temp_object)

        for i in range(len(temp_object)):
            self._sum_values[i] += temp_object[i]
            if temp_object[i] > self._max_values[i]:
                self._max_values[i] = temp_object[i]
            if temp_object[i] < self._min_values[i]:
                self._min_values[i] = temp_object[i]
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
    result._id_of_the_objects = []
    result._data_set = []
    result._used_ids = set()
    result._max_values = []
    result._min_values = []
    result._sum_values = []

    return result


def create_dataset_without_names(dimension_count=3, has_id = True):
    if isinstance(dimension_count, int) and dimension_count>0:
        dimension_names = ["ID"] if has_id else []
        for i in range(1, dimension_count+1):
            dimension_names.append("X"+str(i))
        return create_dataset_with_names(dimension_names, has_id)
    else:
        return None