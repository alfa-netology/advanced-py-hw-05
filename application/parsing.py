import re

PHONE_SEARCH_PATTERN = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.\s\d+)*[\)]*'
PHONE_SUB_PATTERN = r'+7(\2)-\3-\4-\5 \6'

def raw_data(data):
    result = list()
    for row in data:
        record = list()

        full_name = re.findall(r'(\w+)', ' '.join(row[:3]))
        if len(full_name) < 3:
            full_name.append('')

        record += full_name
        record.append(row[3])
        record.append(row[4])
        record.append(re.sub(PHONE_SEARCH_PATTERN, PHONE_SUB_PATTERN, row[5]).strip())
        record.append(row[6])
        result.append(record)
    return result

def make_pure_contact_list(data):
    result = dict()
    for item in data:
        key = item[0]
        if key in result:
            record = merge_doubles(item, result[key])
            result[key] = record
        else:
            result[key] = item
    return result.values()

def merge_doubles(record_one, record_two):
    result = []
    for index in range(len(record_one)):
        result.append(record_one[index]) if record_one[index] else result.append(record_two[index])
    return result
