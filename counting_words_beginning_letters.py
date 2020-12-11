from collections import Counter

with open('DATA/words.txt') as words_in:
    letters = [word[0] for word in words_in]

print(letters[:100], '\n')
print(len(letters))

letter_counts = Counter(letters)

print(letter_counts)

print(letter_counts.most_common(5))


