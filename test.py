import tests.data.maindata_test

# main data test

vis_data_set_test = tests.data.maindata_test.VisDataSetWithIDTest()
vis_data_set_test.create_functions_test1()
vis_data_set_test.dataset_basic_test1()
vis_data_set_test.dataset_basic_test2()
vis_data_set_test.get_object_test()

vis_data_set_test = tests.data.maindata_test.VisDataSetWithoutIDTest()
vis_data_set_test.create_functions_test1()
vis_data_set_test.dataset_basic_test1()
vis_data_set_test.dataset_basic_test2()
vis_data_set_test.get_object_test()

import tests.input.importcsv_test

import_csv_test = tests.input.importcsv_test.ImportCSVFileTest()
import_csv_test.test_no_file()
import_csv_test.test_file(0)
import_csv_test.test_file(1)
import_csv_test.test_file(2)
import_csv_test.test_file(3)
