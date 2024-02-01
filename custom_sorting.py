
fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

f1 = sorted(fruits, key=str.lower)
print(f"{f1 = }\n")

f2 = sorted(fruits, key=len)
print(f"{f2 = }\n")

def len_and_name(item):
    return len(item), item.lower()

f3 = sorted(fruits, key=len_and_name)
print(f"{f3 = }\n")

def wacky_sort(fruit):
    sort_value = fruit[-1]
    print(f"comparing {fruit} as {sort_value}")
    return sort_value

f4 = sorted(fruits, key=wacky_sort)
print(f"{f4 = }\n")
print('-' * 60)


people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print('-' * 60)

def by_dob(person):
    return person[3]

for person in sorted(people, key=by_dob):
    print(person)
print('-' * 60)

def by_last_first(item):
    return item[1], item[0]  # compare 1st item, then 2nd

for person in sorted(people, key=by_last_first):
    print(person)
print('-' * 60)

#  lambda param ...: return-value

for person in sorted(people, key=lambda p: p[3]):
    print(person)
print('-' * 60)

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

for code, city in sorted(airports.items()):
    print(code, city)
print('-' * 60)

print(f"{airports.items() = }\n")

def by_value(item):
    return item[1], item[0]

for code, city in sorted(airports.items(), key=by_value):
    print(code, city)

print(f"{fruits = }\n")

f4 = sorted(fruits, key=str.lower, reverse=True)
print(f"{f4 = }\n")

print(f"{fruits = }\n")

fruits.sort(key=str.lower)
print(f"{fruits = }\n")



