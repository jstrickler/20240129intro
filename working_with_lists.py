
cities = []
cities.append("Schenectady")
cities.append("Colonie")
cities.append("Albany")

more_cities = ["Pittsburgh", "Sewickley", "Monroeville"]

cities.extend(more_cities)
print(f"{cities = }")

cities.insert(0, "Baldwin")
cities.insert(3, "Beaver Falls")

print(f"{cities = }")

#   LIST.append(obj)  LIST.insert(pos, obj)  LIST.extend(iterable)

del cities[2]
print(f"{cities = }")

cities.remove('Beaver Falls')
print(f"{cities = }")

city = cities.pop()
print(f"{city = }")
print(f"{cities = }")

city = cities.pop(2)
print(f"{city = }")
print(f"{cities = }")

#  push/pop


#   DEL LIST[pos]    LIST.remove(value)      LIST.pop(pos)  LIST.pop()

print(f"{cities[:3] = }")
print('-' * 60)

# for VAR in ITERABLE:
#     ...

for city in cities:
    print(city)
print()

animal = "wombat"
for letter in animal:
    print(letter)
print()




