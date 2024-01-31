file_path = "DATA/breakfast.txt"

with open(file_path) as food_in:
    foods = food_in.read().splitlines()

print(foods, '\n')
unique_foods = set(foods)
print(f"{unique_foods = }")

s1 = set()  # empty set
s2 = {5, 9, 18}  # literal set assigned to s2
s3 = set(foods)

colors_a = ['pink', 'blue', 'purple', 'orange', 'white']
colors_b = ['purple', 'purple', 'green', 'blue', 'purple', 'purple', 'pink']

# set: {item, item, item}
# dict: {key:value, key:value, key:value}

set_a = set(colors_a)
set_b = set(colors_b)
print(f"{set_a = }")
print(f"{set_b = }")
set_a.add('scarlet')


print("common:", set_a & set_b)   # intersection
print("not common:", set_a ^ set_b)  # xor
print("both:", set_a | set_b)  # union
print("only in a:", set_a - set_b)
print("only in b:", set_b - set_a)

print(f"{len(set_a) = }")
print(f"{len(set_b) = }")






