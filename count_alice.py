#  set counter to 0
#  for each line in alice.txt
#     if 'Alice' in line
#        increment counter
FILE_PATH = 'DATA/alice.txt'

alice_count = 0
with open(FILE_PATH) as alice_in:
    for line in alice_in:
        if 'Alice' in line:
            alice_count += 1

print(f"{alice_count} lines contained 'Alice'")