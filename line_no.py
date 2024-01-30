# for each file on the command line
#    for each line in the file
#        print line with line number
import sys

for file_path in sys.argv[1:]:  # for each file specified
    # print(file_path)
    # line_number = 1
    with open(file_path) as file_in:   # open file
        for line_number, line in enumerate(file_in, 1): # for index, line in file
            print(f"{line_number:3d} {line.rstrip()}")
            # line_number += 1
    print("-" * 20)
