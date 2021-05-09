from application import data, parsing

if __name__ == '__main__':
    raw_data_path = 'data/phonebook_raw.csv'
    raw_contact_list = data.get_raw(raw_data_path)

    contact_list_with_doubles = parsing.raw_data(raw_contact_list)
    pure_contact_list = parsing.make_pure_contact_list(contact_list_with_doubles)
    pure_data_path = 'data/phonebook_pure.csv'

    data.save_pure(pure_contact_list, pure_data_path)
