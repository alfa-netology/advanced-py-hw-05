import csv

def get_raw(raw_data_path):
    with open(raw_data_path, encoding='utf-8') as file:
        rows = csv.reader(file, delimiter=",")
        result = list(rows)
    return result

def save_pure(data, pure_data_path):
    with open(pure_data_path, "w", encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(data)

