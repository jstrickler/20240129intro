#  for each line in alt.txt
#  if line starts with 'a'
#     write to a.txt
#  if line starts with 'b'
#     write to b.txt
INPUT_FILE = "DATA/alt.txt"
OUTPUT_A = "a.txt"
OUTPUT_B = "b.txt"

with open(INPUT_FILE) as alt_in:
    with open(OUTPUT_A, "w") as a_out:
        with open(OUTPUT_B, "w") as b_out:
            for line in alt_in:
                if line.startswith('a'):
                    a_out.write(line)
                elif line.startswith('b'):
                    b_out.write(line)

