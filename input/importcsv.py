import csv
import data.maindata
import os.path


def import_csv_file(path_to_file="", has_names=False, has_ids=False, delimiter=','):
    if not os.path.exists(path_to_file):
        return None

    input_file = open(path_to_file)
    csvreader = csv.reader(input_file, delimiter=delimiter)
    if has_names:
        names_row = next(csvreader)
        dataset = data.maindata.create_dataset_with_names(names_row, has_id=has_ids)
    else:
        first_row = next(csvreader)
        dataset = data.maindata.create_dataset_without_names(len(first_row)-1 if has_ids else len(first_row),
                                                             has_id=has_ids)
        if has_ids:
            temp = [float(first_row[i]) for i in range(1, len(first_row))]
            temp.insert(0, first_row[0])
            dataset.add_object(temp)
        else:
            dataset.add_object([float(first_row[i]) for i in range(len(first_row))])

    for row in csvreader:
        if has_ids:
            temp = [float(row[i]) for i in range(1, len(row))]
            temp.insert(0, row[0])
            dataset.add_object(temp)
        else:
            dataset.add_object([float(row[i]) for i in range(len(row))])
    input_file.close()
    return dataset
