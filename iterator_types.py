
colors = ['red', 'blue', 'pink', 'ecru', 'orange', 'black', 'white']
people = ['Mary', 'Fred', 'Otto', 'Ali', 'Renaldo']
animals = ['wombat', 'aye-aye', 'pine marten', 'honey badger', 'narwhal']

scolors = sorted(colors)
print(f"{scolors = }\n")

# ITERABLE is any object that can be looped over
# ITERATOR is an object that provides values but does not contain them (generator)


rcolors = reversed(colors)   # reversed is an ITERATOR
print(f"{rcolors = }")

for color in rcolors:
    print(color)
print()

for color in rcolors:
    print(color)
print()

combo = zip(colors, people, animals)
print(f"{combo = }")

for color, person, animal in combo:
    print(color, person, animal)
