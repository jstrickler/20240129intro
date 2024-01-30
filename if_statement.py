value = 82

# if elif else while for def class try except finally with 

if value > 75:
    print("wombat")
    print("wallaby")
    if value > 90:
        print("cane toad")
elif value > 50:  # else if
    print("koala")
    print("kangaroo")
else:
    print("platypus")
    print("quokka")

print("ALL DONE")

# X is FALSE if
# X == 0 or X == 0.0
# X is False
# len(X) == 0  containers (list, str, tuple, bytes, set, dict, ...)
# X is None

m = 39

if m:
    print("MMMMmmmmmmmmm")

#   A ? B : C  non-Python
#   B if A else C   Python

debug = True

color = "red" if debug else "blue"

# my_list = get_some_data()
# if my_list: # if my_list is not empty
#     print("...")
# else:  # my_list IS empty
#     print("no data")


#  == != < > <= >=  is

# if x is y:  are x and y the same object

x = 5
y = x
print(x is y, x == y)

names1 = ['Fred', 'Howard', 'Molly']
names2 = ['Fred', 'Howard', 'Molly']
print(names1 is names2, names1 == names2)

m = None
# ...
if m is None:
    print("...")

#  not  and  or

x = not m

#    obj1 and obj2      True only if both objects are true, False otherwise
#    obj1 or obj2       False only if both objects are false, True otherwise







