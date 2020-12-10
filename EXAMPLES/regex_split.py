#!/usr/bin/env python

import re

rx_wordsep = re.compile(r"[^a-z]+", re.I)  # <1>

s1 = '''There are 10 kinds of people in a Binary world, I hear" -- Geek talk'''

with open('../DATA/alice.txt') as alice_in:
    alice_text = alice_in.read()

words = rx_wordsep.split(s1)  # <2>
print(words)

alice_words = rx_wordsep.split(alice_text)

print(alice_words)
print(len(alice_words))

lower_words = [word.lower() for word in alice_words]
unique_words = set(lower_words)
print(len(unique_words))
print(sorted(unique_words))


