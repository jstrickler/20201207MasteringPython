
try:
    with open('wombat_tricks.txt') as wombats_in:
        pass
except FileNotFoundError as err:
    print(err)

data = ['a', 'b', 'c']
try:
    print(data[17])
except IndexError as err:
    print(err)

values = 0, 5, 8.2, 'abc', 1.17, 0, 5.5, 42, '123', 9, 0

for v in values:
    try:
        v = float(v)
        result = 35 / v
    except ZeroDivisionError as err:
        print(err)
        # log ERROR
    except ValueError as err:
        print(err)
        # log WARNING
    except Exception as err:
        print("Huh!", err)
        # log error here
    else:
        print(result)

