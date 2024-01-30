LIMIT = 1000

flags = [True] * (LIMIT + 1)
print(f"{flags[:10] = }\n")


for num in range(2, LIMIT + 1):
    if flags[num]:  # num must be prime
        print(num, end=" ")
        for m in range(num, LIMIT + 1, num):  # multiples must be non-prime, so set to False
            flags[m] = False
print()