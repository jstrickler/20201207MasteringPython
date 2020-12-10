#!/usr/bin/env python

import sys

try:
    raw_input = input("Enter Celsius temp: ")
    celsius = float(raw_input)
except ValueError as e:
    print("Error!", e)
    sys.exit(1)
else:
    fahrenheit = ((9 * celsius) / 5) + 32
    print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))

