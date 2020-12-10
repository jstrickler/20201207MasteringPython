d1 = dict()

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'YUL': 'Montreal',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

d2 = {}  # empty dict

print(airports['YOW'])
print(airports.get('LAX'))
print(airports.get('LAX', 'NOT FOUND'))

airports['ELM'] = "Elmyra"
airports['INT'] = "Winston-Salem"

key = 'OAK'
if key in airports:
    del airports[key]

print(len(airports))

print(airports, '\n')

print(airports.keys(), '\n')
print(airports.values(), '\n')

print(airports.items(), '\n')

for airport_code, airport_name in airports.items():
    print(airport_code, airport_name)
print()






