# print powers of two from 2^0 through 2^31

for exponent in range(0, 32):
    power = 2 ** exponent
    print(f"{exponent:2d} {power:10d}")

name = "Bob"
animal = "marmot"

s = f"{name} has a pet {animal}"
print(f"{s = }")
