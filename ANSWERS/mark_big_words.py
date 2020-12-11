#!/usr/bin/env python

import re

rx_longword = re.compile(r"\b[a-z]{8,}\b", re.I)


def mark_word(m):
    return '**' + m.group() + '**'


with open('../DATA/parrot.txt') as parrot_in:
    with open('bigwords.txt', 'w') as bigwords_out:
        old_text = parrot_in.read()
        new_text = rx_longword.sub(mark_word, old_text)  # find each match and replace by calling mark_word()
        bigwords_out.write(new_text)


