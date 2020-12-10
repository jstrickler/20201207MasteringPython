#!/usr/bin/python3

def cleanup():
    pass

spam = [
    "Spam",
    "eggs  ",
    "   spam    ",
    "     spam spam     ",
    "SPAM	",
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]

for s in spam:
    result = cleanup(s)
    print(s, result)
