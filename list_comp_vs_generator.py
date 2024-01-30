fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

fruit_list = [f.upper() for f in fruits]  # normal list
print(f"{fruit_list = }\n")

fruit_gen = (f.title() for f in fruits)  # generator which MUST be looped over
print(f"{fruit_gen = }")
for fruit in fruit_gen:
    print(fruit)