import csv

with open('DATA/titanic.csv') as titanic_in:
    rdr = csv.reader(titanic_in)
    headers = next(rdr)  # read 1st line
    titanic_data = list(rdr)
    for row in titanic_data[:5]:
        print(row)
    