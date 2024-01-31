from pprint import pprint

file_path = 'DATA/knights.txt'

knight_data = {}
with open(file_path) as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = title, color, quest, comment

pprint(knight_data)
print()

for name, data in knight_data.items():
    print(data[0], name)
print()

print(knight_data['Gawain'] 
