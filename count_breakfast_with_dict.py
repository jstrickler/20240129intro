file_path = "DATA/breakfast.txt"

food_count = {}

with open(file_path) as food_in:
    foods = food_in.read().splitlines()

for food in foods:
    if food in food_count:  # if food in dict
        food_count[food] += 1   # increment value  food_count[food] = food_count[food] + 1
    else:
        food_count[food] = 1   # add to dict

for food, count in food_count.items():
    print(food, count)
