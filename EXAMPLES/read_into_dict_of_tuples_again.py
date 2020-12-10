#!/usr/bin/env python
from pprint import pprint

def main():
    data = read_data()
    pretty_print(data)
    print_name_and_title(data)


def read_data():
    knight_info = {}  # <1>

    with open("../DATA/knights.txt") as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            (name, title, color, quest, comment) = line.split(":")
            knight_info[name] = title, color, quest, comment  # <2>
    return knight_info


def pretty_print(info):
    pprint(info)
    print()


def print_name_and_title(info):
    for name, data in info.items():
        print(data[0], name)

print("My name is", __name__)

if __name__ == '__main__':
    main()
