import maindata


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


class VisDataSetWithIDTest:
    _data_set11 = ["first", 1, 1, 1, 1]
    _data_set12 = ["second", 2, 2, 2, 2]
    _data_set13 = ["third", -3.4, 6, 3, 0]
    _data_set14 = ["fourth", 1, 1, 1, 1]
    _data_set_fail1 = ["test", "1", 1, 1, 1]
    _data_set_fail2 = ["test", [1, 2], 1, 1, 1]
    _data_set1_max = [2, 6, 3, 2]
    _data_set1_min = [-3.4, 1, 1, 0]
    _data_set1_sum = [0.6, 10, 7, 4]

    def create_functions_test1(self):
        assert maindata.create_dataset_with_names(None) is None
        assert maindata.create_dataset_without_names(0) is None
        assert maindata.create_dataset_without_names(-23) is None
        assert maindata.create_dataset_without_names("asd") is None
        test_dataset = maindata.create_dataset_without_names(4)
        assert test_dataset.add_object(["name", 1, 2, 3, 4])
        assert not test_dataset.add_object(["name", 1, 3, 4])
        assert not test_dataset.add_object(self._data_set_fail1)
        assert not test_dataset.add_object(self._data_set_fail2)

    def create_testdataset1(self):
        test_dataset = maindata.create_dataset_without_names(4)
        test_dataset.add_object(self._data_set11)
        test_dataset.add_object(self._data_set12)
        test_dataset.add_object(self._data_set13)
        test_dataset.add_object(self._data_set14)
        return test_dataset

    def create_testdataset2(self):
        test_dataset = maindata.create_dataset_with_names(["Iden", "X", "Y", "Z", "T"])
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
    _data_set11 = [1, 1, 1, 1]
    _data_set12 = [2, 2, 2, 2]
    _data_set13 = [-3.4, 6, 3, 0]
    _data_set14 = [1, 1, 1, 1]
    _data_set_fail1 = ["1", 1, 1, 1]
    _data_set_fail2 = [[1, 2], 1, 1, 1]
    _data_set1_max = [2, 6, 3, 2]
    _data_set1_min = [-3.4, 1, 1, 0]
    _data_set1_sum = [0.6, 10, 7, 4]

    def create_functions_test1(self):
        assert maindata.create_dataset_with_names(None, has_id=False) is None
        assert maindata.create_dataset_without_names(0, has_id=False) is None
        assert maindata.create_dataset_without_names(-23, has_id=False) is None
        assert maindata.create_dataset_without_names("asd", has_id=False) is None
        test_dataset = maindata.create_dataset_without_names(4, has_id=False)
        assert test_dataset.add_object([1, 2, 3, 4])
        assert not test_dataset.add_object([1, 3, 4])
        assert not test_dataset.add_object(self._data_set_fail1)
        assert not test_dataset.add_object(self._data_set_fail2)

    def create_testdataset1(self):
        test_dataset = maindata.create_dataset_without_names(4, has_id=False)
        test_dataset.add_object(self._data_set11)
        test_dataset.add_object(self._data_set12)
        test_dataset.add_object(self._data_set13)
        test_dataset.add_object(self._data_set14)
        return test_dataset

    def create_testdataset2(self):
        test_dataset = maindata.create_dataset_with_names(["X", "Y", "Z", "T"], has_id=False)
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


import basicnumbers


class VisDataSetCalculationTest:
    _test_dataset = [[[[1, 1, 1, 1], [2, 2, 2, 2], [-3.4, 6, 3, 0], [1, 1, 1, 1]],
                      [2, 6, 3, 2], [-3.4, 1, 1, 0], [0.6, 10, 7, 4], [0.15, 2.5, 1.75, 1]],
                     [[[5.2, 3.2, 2.2, 4.1], [-5.2, -3.2, -2.2, -4.1], [1, 1, 1, 1], [3, 2, 4, 5]],
                      [5.2, 3.2, 4, 5], [-5.2, -3.2, -2.2, -4.1], [4, 3, 5, 6], [1, 0.75, 1.25, 1.5]]]

    def create_testdataset(self, num):
        dataset = maindata.create_dataset_without_names(4, False)
        for i in range(len(self._test_dataset[num][0])):
            dataset.add_object(self._test_dataset[num][0][i])
        return dataset

    def run_basic_numbers(self, num):
        dataset = self.create_testdataset(num)
        calc_task = basicnumbers.BasicNumbersCalculation()
        assert dataset.apply_calculation(calc_task, []) is None
        assert dataset.calculation_ready
        if dataset.calculation_ready:
            result = dataset.apply_calculation(calc_task, [])
            for i in range(len(self._test_dataset[num][1])):
                assert isclose(result[0][i], self._test_dataset[num][1][i])
            for i in range(len(self._test_dataset[num][2])):
                assert isclose(result[1][i], self._test_dataset[num][2][i])
            for i in range(len(self._test_dataset[num][3])):
                assert isclose(result[2][i], self._test_dataset[num][3][i])
            for i in range(len(self._test_dataset[num][4])):
                assert isclose(result[3][i], self._test_dataset[num][4][i])


import normalize


class VisDataSetChangeTest:
    _test_dataset = [[[[-1, 2, 3, 4], [4, 3, 2, -2], [2, 4, 6, 8], [2, 6, 7, 1]],
                      [[0, 0, 3, 5], [5, 10, 10, 6]],
                      True,
                      [[0, 0, 4.4, 5.6], [5, 2.5, 3, 5], [3, 5, 8.6, 6], [3, 10, 10, 5.3]]],
                     [[[2, -1, 5, 5], [-5, 1, -5, 2], [0, 0, -4, -1], [5, -5, 5, -5]],
                      [[0, -1, -2, -3], [4, 2, 2, 0]],
                      True,
                      [[2.8, 1, 2, 0], [0, 2, -2, -0.9], [2, 1.5, -1.6, -1.8], [4, -1, 2, -3]]],
                     [[[-5, -5, 0, -5], [0, -2, 2, 2], [3, -4, -5, -5], [5, -5, 5, -5]],
                      [[-2, 0, -5, -5], [0, 3, 0, 5]],
                      True,
                      [[-2, 0, -2.5, -5], [-1, 3, -1.5, 5], [-0.4, 1, -5, -5], [0, 0, 0, -5]]]]

    def create_testdataset(self, num):
        dataset = maindata.create_dataset_without_names(4, False)
        for i in range(len(self._test_dataset[num][0])):
            dataset.add_object(self._test_dataset[num][0][i])
        return dataset

    def run_change_data_test(self, num):
        dataset = self.create_testdataset(num)
        change_task = normalize.NormalizeData()
        assert dataset.apply_changes(change_task, self._test_dataset[num][1]) is None
        assert dataset.calculation_ready
        if dataset.calculation_ready:
            result = dataset.apply_changes(change_task, self._test_dataset[num][1])
            assert result == self._test_dataset[num][2]
            if result:
                for i in range(len(self._test_dataset[num][3])):
                    test_result = dataset.get_object_by_number(i)
                    for j in range(len(test_result[1])):
                        result = isclose(test_result[1][j], self._test_dataset[num][3][i][j])
                        assert result




def run_maindata_test():
    print("Testing data set without ID methods:")
    vis_data_set_test = VisDataSetWithIDTest()
    print("Testing create functions:")
    vis_data_set_test.create_functions_test1()
    print("Passed")
    print("Testing basic functions number 1:")
    vis_data_set_test.dataset_basic_test1()
    print("Passed")
    print("Testing basic functions number 2:")
    vis_data_set_test.dataset_basic_test2()
    print("Passed")
    print("Testing get object functions:")
    vis_data_set_test.get_object_test()
    print("Passed")

    print("Testing data set with ID methods:")
    vis_data_set_test = VisDataSetWithoutIDTest()
    print("Testing create functions:")
    vis_data_set_test.create_functions_test1()
    print("Passed")
    print("Testing basic functions number 1:")
    vis_data_set_test.dataset_basic_test1()
    print("Passed")
    print("Testing basic functions number 2:")
    vis_data_set_test.dataset_basic_test2()
    print("Passed")
    print("Testing get object functions:")
    vis_data_set_test.get_object_test()
    print("Passed")

    print("Testing data set calculation methods:")
    calculation_test = VisDataSetCalculationTest()
    for i in range(len(calculation_test._test_dataset)):
        print(f"Testing dataset number {i}:")
        calculation_test.run_basic_numbers(i)
        print("Passed")

    print("Testing data set change methods:")
    change_test = VisDataSetChangeTest()
    for i in range(len(change_test._test_dataset)):
        print(f"Testing dataset number {i}:")
        change_test.run_change_data_test(i)
        print("Passed")
