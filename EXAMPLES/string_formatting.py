city = 'Orlando'
temp = 85
count = 5
avg = 3.4563892382


print("It is {}\u00B0 in {}".format(temp, city))  # variables inserted into string
print(f"IT is {temp}\u00B0 in {city}")  # same, but better!

# .2f means round a float to 2 decimal points
print("count is {:03d} avg is {:.2f}".format(count, avg))

print("2 + 2 is {}".format(2 + 2))  # any expression is OK
