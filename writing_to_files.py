fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in sorted(fruits):
        fruits_out.write(f"{fruit.title()}\n")  #   fruit + '\n'
    # fruits_out automatically closed here...

with open('DATA/breakfast.txt') as breakfast_in:
    with open('nospam.txt', "w") as nospam_out:
        for line in breakfast_in:
            if line.startswith('spam'):
                continue
            nospam_out.write(line.title())


colors = ['red', 'green', 'purple', 'orange', 'brown',
'black', 'olive', 'navy', 'white', 'black',
'pink', 'chartreuse']

for i, color in enumerate(colors, 1):
    print(i, color)




