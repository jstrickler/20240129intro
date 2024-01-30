import sys

# sys.argv[0] is script name

word_to_find = sys.argv.pop(1)

for file_path in sys.argv[1:]:
    word_count = 0
    with open(file_path) as file_in:
        for line in file_in:
            if word_to_find in line:
                word_count += 1
    print(f"{file_path}: {word_count}")
