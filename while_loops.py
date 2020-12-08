

i = 0
while i < 3:
    print(i)
    i += 1
print()

while True:  # loop "forever"
    raw_rating = input("Enter rating (1-5): ")
    if raw_rating == 'q':
        break
    elif raw_rating == '':
        continue
    else:
        rating = int(raw_rating)
        print('*' * rating)
