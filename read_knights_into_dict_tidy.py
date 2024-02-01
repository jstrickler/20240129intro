"""
Read knight data into array and print the data in various ways
"""
from pprint import pprint

FILE_PATH = 'DATA/knights.txt'

def main():
    data = read_knight_data()
    pretty_print_knight_data(data)
    print()
    print_knight_titles_and_names(data)
    print()
    print(get_knight_field(data, 'Robin', 3))

def read_knight_data():
    knight_data = {}
    with open(FILE_PATH) as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            knight_data[name] = title, color, quest, comment
    return knight_data

def pretty_print_knight_data(data):
    pprint(data)

def print_knight_titles_and_names(data):
    for name, fields in data.items():
        print(fields[0], name)

def get_knight_field(data, knight, field_number):
    return data[knight][field_number]


main()