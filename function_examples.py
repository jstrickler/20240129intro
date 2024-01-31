def say_hello():
    print("Hello, Python world!")

say_hello()
say_hello()

def hello_whomever(whom="world"):
    print(f"Hello, {whom}")

hello_whomever('world')
hello_whomever('you crazy moon')
hello_whomever('wombat')
hello_whomever()

def read_files(p1, *file_paths):
    for file_path in file_paths:
        print("reading", file_path)


read_files("NC", 'carrot.txt')
read_files("CO", 'blue.txt', 'green.txt', 'wombat.txt', 'cucumber.txt')
read_files("FL")