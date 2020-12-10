
word_counts = {}

with open('DATA/words.txt') as words_in:
    for line in words_in:
        letter = line[-2]  # get first letter of word
        if letter not in word_counts:
            word_counts[letter] = 0

        word_counts[letter] = word_counts[letter] + 1
        #  word_counts[letter] += 1

for letter, count in word_counts.items():
    print(letter, count)


