import sqlite3

file_path = "DATA/wombats.txt"

try:
    with open(file_path) as file_in:
        for raw_line in file_in:
            line = raw_line.rstrip()
            print(line)
except (FileNotFoundError, PermissionError) as err:
    print(err)
print()

nums = [800, 80, 0.0, 1000, 32, -4, 255, -8, 0, 400, 5, 5000]

for num in nums:
    try:
        result = 10000 / num
    except ZeroDivisionError as err:
        print(err)  # should log this error
    else:  # if no exceptions are raised
        print(result)


print("ALL DONE")

conn = None
cur = None

try:
    conn = sqlite3.connect('wombats.db')
    cur = conn.cursor()
except sqlite3.Error as err:
    print(err)
    print("Program quitting")
    exit()
else:
    cur.execute("select * from wombats")
    results = cur.fetchall()
finally:
    if cur:
        cur.close()
    if conn:
        conn.close()




