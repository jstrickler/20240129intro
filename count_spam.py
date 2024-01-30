FILE_PATH = "DATA/breakfast.txt"

spam_count = 0
with open(FILE_PATH) as file_in:
    for line in file_in:
        if line.startswith('spam'):
            spam_count += 1  # add 1 to spam_count

print(f"{spam_count = }")

with open(FILE_PATH) as file_in:
    contents = file_in.read()
    spam_count = contents.count('spam')
print(f"{spam_count = }")
