import csv

def get_raw(source):
    with open(source, encoding='utf-8') as file:
        rows = csv.reader(file, delimiter=",")
        result = list(rows)
    return result

def save_pure_data(data):
    with open("data/phonebook_pure.csv", "w", newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(data)

