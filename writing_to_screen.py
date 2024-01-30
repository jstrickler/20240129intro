person = "Taylor Swift"
city = "New York"
value = 38.31938923833832

print(person, city, value)  # str(person) + " " + str(city) + " " + str(value) + "\n"
print("=====")
print(person, city, value, sep="#")
print(person, city, value, sep=", ")
print(person, city, value, sep="&")

print(person, end=" ")
# if ...
print(city, end=" ")
# if ...
print(value)
print()   # just print \n

# city: person
print(city, ":", person)

print(f"{city}: {person}")
print(f"{person} lives in {city}!")
print(f"2 + 2 is {2 + 2}")

x =  5
print("x =", x)
print(f"{x = :04d}")
print(f"{x = :8d}")


