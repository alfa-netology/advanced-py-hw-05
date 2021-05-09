from application import data, parsing

if __name__ == "__main__":
    data_source = 'data/phonebook_raw.csv'
    raw_contact_list = data.get_raw(data_source)
    contact_list_with_doubles = parsing.raw_data(raw_contact_list)
    pure_contact_list = parsing.make_pure_contact_list(contact_list_with_doubles)
    data.save_pure(pure_contact_list)
