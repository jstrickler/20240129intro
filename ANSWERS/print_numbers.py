import re

with open("../DATA/custinfo.dat") as f:
    for line in f:
        m = re.search(r"\b\d{3}-\d{4}\b", line)
        if m:
            print(m.group(), line, end='')

