import re

#  x = foo()
#  b = Bar()

# obj = class()
# instance = class()
colors = list()
print(f"{type(list) = }")
print(f"{type(colors) = }")

# list.append(colors, "red")
colors.append("red")
colors.append('pink')
colors.insert(0, 'green')
print(f"{colors = }")

cities = list()

x = 5      #   x = int(5)

spam = "wombat"   #  spam = str("wombat")

print(f"{type(re) = }")

class Animal:
    def run(self):
        print("running, running")

class Dog(Animal):
    def bark(self):
        print("woof! woof!")

d1 = Dog()
d1.bark()
d1.run()

d2 = Dog()
d2.bark()
d3 = Dog()
d3.run()






