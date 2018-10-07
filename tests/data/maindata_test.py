import data.maindata

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

class VisDataSetWithIDTest:
    _data_set11=["first", 1, 1, 1, 1]
    _data_set12=["second", 2, 2, 2, 2]
    _data_set13=["third", -3.4, 6, 3, 0]
    _data_set14=["fourth", 1, 1, 1, 1]
    _data_set_fail1=["test", "1", 1, 1, 1]
    _data_set_fail2=["test", [1,2], 1, 1, 1]
    _data_set1_max=[2, 6, 3, 2]
    _data_set1_min=[-3.4, 1, 1, 0]
    _data_set1_sum=[0.6, 10, 7, 4]

    def create_functions_test1(self):
        assert data.maindata.create_dataset_with_names(None) is None
        assert data.maindata.create_dataset_without_names(0) is None
        assert data.maindata.create_dataset_without_names(-23) is None
        assert data.maindata.create_dataset_without_names("asd") is None
        test_dataset = data.maindata.create_dataset_without_names(4)
        assert test_dataset.add_object(["name",1,2,3,4])
        assert not test_dataset.add_object(["name",1,3,4])
        assert not test_dataset.add_object(self._data_set_fail1)
        assert not test_dataset.add_object(self._data_set_fail2)

    def create_testdataset1(self):
        test_dataset = data.maindata.create_dataset_without_names(4)
        test_dataset.add_object(self._data_set11)
        test_dataset.add_object(self._data_set12)
        test_dataset.add_object(self._data_set13)
        test_dataset.add_object(self._data_set14)
        return test_dataset

    def create_testdataset2(self):
        test_dataset = data.maindata.create_dataset_with_names(["Iden", "X", "Y", "Z", "T"])
        test_dataset.add_object(self._data_set11)
        test_dataset.add_object(self._data_set12)
        test_dataset.add_object(self._data_set13)
        test_dataset.add_object(self._data_set14)
        return test_dataset

    def dataset_basic_test1(self):
        test_dataset = self.create_testdataset1()
        for i in range(len(test_dataset._max_values)):
            assert isclose(test_dataset._max_values[i], self._data_set1_max[i])
        for i in range(len(test_dataset._min_values)):
            assert isclose(test_dataset._min_values[i], self._data_set1_min[i])
        for i in range(len(test_dataset._sum_values)):
            assert isclose(test_dataset._sum_values[i], self._data_set1_sum[i])
        assert test_dataset._names_of_dimensions == ["ID", "X1", "X2", "X3", "X4"]

    def dataset_basic_test2(self):
        test_dataset = self.create_testdataset2()
        for i in range(len(test_dataset._max_values)):
            assert isclose(test_dataset._max_values[i], self._data_set1_max[i])
        for i in range(len(test_dataset._min_values)):
            assert isclose(test_dataset._min_values[i], self._data_set1_min[i])
        for i in range(len(test_dataset._sum_values)):
            assert isclose(test_dataset._sum_values[i], self._data_set1_sum[i])
        assert test_dataset._names_of_dimensions == ["Iden", "X", "Y", "Z", "T"]

    def get_object_test(self):
        test_dataset = self.create_testdataset1()
        assert test_dataset.get_object_by_id("first") == ["first", [1, 1, 1, 1], None]
        assert test_dataset.get_object_by_id("third") == ["third", [-3.4, 6, 3, 0], None]
        assert test_dataset.get_object_by_number(1) == ["second", [2, 2, 2, 2], None]





class VisDataSetWithoutIDTest:
    _data_set11=[1, 1, 1, 1]
    _data_set12=[2, 2, 2, 2]
    _data_set13=[-3.4, 6, 3, 0]
    _data_set14=[1, 1, 1, 1]
    _data_set_fail1=["1", 1, 1, 1]
    _data_set_fail2=[[1,2], 1, 1, 1]
    _data_set1_max=[2, 6, 3, 2]
    _data_set1_min=[-3.4, 1, 1, 0]
    _data_set1_sum=[0.6, 10, 7, 4]

    def create_functions_test1(self):
        assert data.maindata.create_dataset_with_names(None, has_id=False) is None
        assert data.maindata.create_dataset_without_names(0, has_id=False) is None
        assert data.maindata.create_dataset_without_names(-23, has_id=False) is None
        assert data.maindata.create_dataset_without_names("asd", has_id=False) is None
        test_dataset = data.maindata.create_dataset_without_names(4, has_id=False)
        assert test_dataset.add_object([1,2,3,4])
        assert not test_dataset.add_object([1,3,4])
        assert not test_dataset.add_object(self._data_set_fail1)
        assert not test_dataset.add_object(self._data_set_fail2)

    def create_testdataset1(self):
        test_dataset = data.maindata.create_dataset_without_names(4, has_id=False)
        test_dataset.add_object(self._data_set11)
        test_dataset.add_object(self._data_set12)
        test_dataset.add_object(self._data_set13)
        test_dataset.add_object(self._data_set14)
        return test_dataset

    def create_testdataset2(self):
        test_dataset = data.maindata.create_dataset_with_names(["X", "Y", "Z", "T"], has_id=False)
        test_dataset.add_object(self._data_set11)
        test_dataset.add_object(self._data_set12)
        test_dataset.add_object(self._data_set13)
        test_dataset.add_object(self._data_set14)
        return test_dataset

    def dataset_basic_test1(self):
        test_dataset = self.create_testdataset1()
        for i in range(len(test_dataset._max_values)):
            assert isclose(test_dataset._max_values[i], self._data_set1_max[i])
        for i in range(len(test_dataset._min_values)):
            assert isclose(test_dataset._min_values[i], self._data_set1_min[i])
        for i in range(len(test_dataset._sum_values)):
            assert isclose(test_dataset._sum_values[i], self._data_set1_sum[i])
        assert test_dataset._names_of_dimensions == ["X1", "X2", "X3", "X4"]

    def dataset_basic_test2(self):
        test_dataset = self.create_testdataset2()
        for i in range(len(test_dataset._max_values)):
            assert isclose(test_dataset._max_values[i], self._data_set1_max[i])
        for i in range(len(test_dataset._min_values)):
            assert isclose(test_dataset._min_values[i], self._data_set1_min[i])
        for i in range(len(test_dataset._sum_values)):
            assert isclose(test_dataset._sum_values[i], self._data_set1_sum[i])
        assert test_dataset._names_of_dimensions == ["X", "Y", "Z", "T"]

    def get_object_test(self):
        test_dataset = self.create_testdataset1()
        assert test_dataset.get_object_by_id(0) == [0, [1, 1, 1, 1], None]
        assert test_dataset.get_object_by_id(2) == [2, [-3.4, 6, 3, 0], None]
        assert test_dataset.get_object_by_number(1) == [1, [2, 2, 2, 2], None]
