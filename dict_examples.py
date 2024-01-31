from collections import defaultdict
d1 = dict()  # empty dict
d2 = {'NJ': 'Trenton', 'NC': 'Raleigh', 'CA': 'Sacramento'}
d3 = {}  # empty dict

d2['VA'] = 'Richmond'
d2['GA'] = 'Athens'

# ...
d2['GA'] = 'Atlanta'

print(f"{d2['GA'] = }")
print(f"{len(d2) = }")

print(f"{'GA' in d2 = }")
print(f"{'NV' in d2 = }")

del d2['VA']
print(f"{d2 = }")

#  len(any-container)    length

print(f"{d2['NC'] = }")

# print(f"{d2['NY'] = }")
print(f"{d2.get('NY') = }")
print(f"{d2.get('NY', 'NOT FOUND') = }")

print(f"{d2.setdefault('NY', 'Albany') = }")
print(f"{d2 = }")

def zero():
    return 0

data = defaultdict(zero)
data['spam'] = 42
data['ham'] = 98
data['toast'] = 14
print(f"{data = }")
print(f"{data['spam'] = }")
print(f"{data['marmalade'] = }")
print(f"{data = }")
print()

for state, capital in d2.items():
    print(state, capital)
print()

print(f"{d2.items() = }")
print()

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

for code, city in airports.items():
    print(code, city)

print(f"{airports['RDU'] = }")
print()

print(airports.keys())
print()
print(airports.values())
print()


