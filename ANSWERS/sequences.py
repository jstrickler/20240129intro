ctemps = [-40.0, 0.0, 37.0, 75.0, 100.0]

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

temps = []
for c in ctemps:
    f = ((9 * c) / 5) + 32
    print(f"{c:<6.1f} C = {f:6.1f} F")  # min.dec_places

#  {foo:5s}  {foo:5.5s}     min.max 
#  {foo:5s}  {foo:^5s} {foo:>5s}

data = [(0, 32), (-40, -40), (100, 212), (37, 98.6)]
cel_temps = [0, -40, 100, 37]
fahr_temps = [32, -40, 212, 98.6]

for cel, fahr in zip(cel_temps, fahr_temps):
    print(f"{cel:6} {fahr:6}")

print(list(zip(cel_temps, fahr_temps)))



print()

clean_fruits = [f.strip().lower() for f in fruits]

print(clean_fruits)
