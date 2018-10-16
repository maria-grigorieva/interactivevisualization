import input.importcsv


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


class ImportCSVFileTest:
    _test_data = [['tests/dataset/testdata_noid_nonames.csv', False, False],
                  ['tests/dataset/testdata_noid_names.csv', True, False],
                  ['tests/dataset/testdata_id_nonames.csv', False, True],
                  ['tests/dataset/testdata_id_names.csv', True, True]]
    _test_data_basic_results = [[[4.5, 12, 2.3, 12, 2.77],
                                 [-5, -5, -5, 1, 1],
                                 [-1.4, 13.3, 0.7, 18.5, 7.37],
                                 ['X1', 'X2', 'X3', 'X4', 'X5']],
                                [[4.5, 12, 2.3, 12, 2.77],
                                 [-5, -5, -5, 1, 1],
                                 [-1.4, 13.3, 0.7, 18.5, 7.37],
                                 ['X', 'Y', 'Z', 'T', 'G']],
                                [[4.5, 12, 2.3, 12, 2.77],
                                 [-5, -5, -5, 1, 1],
                                 [-1.4, 13.3, 0.7, 18.5, 7.37],
                                 ['ID', 'X1', 'X2', 'X3', 'X4', 'X5']],
                                [[4.5, 12, 2.3, 12, 2.77],
                                 [-5, -5, -5, 1, 1],
                                 [-1.4, 13.3, 0.7, 18.5, 7.37],
                                 ['Names', 'X', 'Y', 'Z', 'T', 'G']]]
    _test_data_object_test = [[[0, [0, [1.2, 1.3, 1.4, 1.5, 1.6], None]],
                               [2, [2, [-2.1, -5, 2, 12, 1], None]],
                               [1, [1, [4.5, 5, 2.3, 1, 2.77], None]]],
                              [[0, [0, [1.2, 1.3, 1.4, 1.5, 1.6], None]],
                               [2, [2, [-2.1, -5, 2, 12, 1], None]],
                               [1, [1, [4.5, 5, 2.3, 1, 2.77], None]]],
                              [['first', ['first', [1.2, 1.3, 1.4, 1.5, 1.6], None]],
                               ['third', ['third', [-2.1, -5, 2, 12, 1], None]],
                               [1, ['second', [4.5, 5, 2.3, 1, 2.77], None]]],
                              [['first', ['first', [1.2, 1.3, 1.4, 1.5, 1.6], None]],
                               ['third', ['third', [-2.1, -5, 2, 12, 1], None]],
                               [1, ['second', [4.5, 5, 2.3, 1, 2.77], None]]]]
    def test_no_file(self):
        assert input.importcsv.import_csv_file('') == None

    def dataset_basic_test(self, test_dataset, results):
        for i in range(len(test_dataset._max_values)):
            assert isclose(test_dataset._max_values[i], results[0][i])
        for i in range(len(test_dataset._min_values)):
            assert isclose(test_dataset._min_values[i], results[1][i])
        for i in range(len(test_dataset._sum_values)):
            assert isclose(test_dataset._sum_values[i], results[2][i])
        assert test_dataset._names_of_dimensions == results[3]

    def get_object_test(self, test_dataset, tests):
        assert test_dataset.get_object_by_number(tests[2][0]) == tests[2][1]
        assert test_dataset.get_object_by_id(tests[0][0]) == tests[0][1]
        assert test_dataset.get_object_by_id(tests[1][0]) == tests[1][1]

    def test_file(self, testnum):
        dataset = input.importcsv.import_csv_file(self._test_data[testnum][0],
                                                  has_names=self._test_data[testnum][1],
                                                  has_ids=self._test_data[testnum][2])
        self.dataset_basic_test(dataset, self._test_data_basic_results[testnum])
        self.get_object_test(dataset, self._test_data_object_test[testnum])

def run_importcsv_test():
    import_csv_test = ImportCSVFileTest()
    import_csv_test.test_no_file()
    import_csv_test.test_file(0)
    import_csv_test.test_file(1)
    import_csv_test.test_file(2)
    import_csv_test.test_file(3)