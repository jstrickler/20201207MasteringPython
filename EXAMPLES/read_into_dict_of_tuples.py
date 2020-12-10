#!/usr/bin/env python
from pprint import pprint

knight_info = {}  # <1>

with open("../DATA/knights.txt") as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        (name, title, color, quest, comment) = line.split(":")
        knight_info[name] = title, color, quest, comment  # <2>

pprint(knight_info)
print()

for name, info in knight_info.items():
    print(info[0], name, info[1])

# print()
# print(knight_info['Robin'][2])
