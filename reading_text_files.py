

mary_in = open('DATA/mary.txt')
mary_in.close()

# /Users/jstrick/Desktop/py3master/DATA/mary.txt
with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    print("normal")
    print(contents)
    print("raw")
    print(repr(contents))
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_without_nl = mary_in.read().splitlines()
    print(all_lines_without_nl)
print('-' * 60)

min_len = 20
with open('DATA/words.txt') as words_in:
    long_words = []
    word_count = 0
    for raw_word in words_in:
        word = raw_word.rstrip()
        if len(word) > min_len:
            word_count += 1
            print(word)
            long_words.append(word)

print(f"{word_count} words longer than 12 characters\n")


with open('long_words.txt', 'w') as longwords_out:
    for word in long_words:
        longwords_out.write(word + '\n')

# read from one file, write to one or more output files
with open('DATA/words.txt') as words_in:
    with open('shortwords.txt', 'w') as shortwords_out:
        with open('longwords.txt', 'w') as longwords_out:
            for line in words_in:
                if len(line) < 7:
                    shortwords_out.write(line)
                elif len(line) > 21:
                    longwords_out.write(line)

import sys
for file_name in sys.argv[1:]:  # loop through files on command line
    with open(file_name) as file_in:
        pass







