
COLOR = "green"   # global variable

def spam():
    # local namespace
    animal = "wombat"  # local variable
    print(f"{COLOR = }")
    

spam()

print(f"{COLOR = }")

# name search:   local nonlocal global builtin

def ham():
    x = 5
    def spam():
        pass
