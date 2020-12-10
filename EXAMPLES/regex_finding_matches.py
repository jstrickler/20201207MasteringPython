#!/usr/bin/env python

import re

s = """lorem ipsum M302 dolor sit amet, consectetur r99 adipiscing elit, sed do
 eiusmod tempor incididunt H476 ut labore et dolore magna Q51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo z883  consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A110 cupidatat non proident, sunt in H332 culpa qui 
officia deserunt Y45 mollit anim id est laborum"""

# group 0   (           )
pattern = r'[A-Z]\d{2,3}'  # <1>

if re.search(pattern, s):  # <2>
    print("Found pattern.")
print()

m = re.search(pattern, s)  # <3>
print(m)
if m:
    print("Found:", m.group(0))  # <4>  or m.group()
print()

for m in re.finditer(pattern, s):  # <5>
    print(m.group())
print()

matches = re.findall(pattern, s)  # <6>
print("matches:", matches)

#  re.match()  assumes ^PATTERN
#  re.fullmatch() assumes ^PATTERN$

p = """
So there's this fella with a parrot. And this parrot swears
like a sailor, I mean he's a pistol. He can swear for five minutes
straight without repeating himself. Trouble is, the guy who owns
him is a quiet, conservative type, and this bird's foul mouth is
driving him crazy.

There are 10 things I hate about you. 5, 4, 3, 2, 1.  

One day, it gets to be too much, so the guy grabs the bird by the
throat, shakes him really hard, and yells, "QUIT IT!" But this just
makes the bird mad and he swears more than ever.

Then the guy gets mad and says, "OK, fork you." and locks the bird
in a kitchen cabinet.

This really aggravates the bird and he claws and scratches,
and when the guy finally lets him out, the bird cuts loose with a
stream of invective that would make a veteran sailor blush.
"""
print()
#             1       2
pattern = r'bi(?P<thing1>rd)|pa(?P<thing2>rr)ot'

for m in re.finditer(pattern, p):
    print(m.group(), m.group('thing1'), m.group('thing2'))
