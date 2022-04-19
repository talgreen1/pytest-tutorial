import csv
import sys

data_file = sys.path[1] + "/../../tests/config/data.csv"


def get_data():
    with open(data_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        data = [tuple(row) for row in reader]
    return data


print(get_data())
