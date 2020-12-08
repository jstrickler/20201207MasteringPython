#!/usr/bin/env python

fruits = ['apple', 'cherry', 'orange', 'kiwi', 'banana', 'pear', 'fig']   # list
name = "Eric Idle"   # string
knight = 'King', 'Arthur', 'Britain'   # tuple
data = b'abc\01'   # byte string (AKA bytes object)

print(fruits[3])  # <1>
print(name[0])  # <2>
print(knight[1])  # <3>
print(data[2])

print(len(fruits), len(name), len(knight), len(data))

numbers = 53

numbers_str = str(53)

print(numbers, numbers_str)

print(numbers_str[0])


