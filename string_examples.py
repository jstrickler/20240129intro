s1 = "spam\n"  
print(len(s1))
print(s1)
s2 = 'spam\n'   # use either "" or ''

print("Guido's the ex-BDFL of Python")
print('Guido is the ex-"BDFL" of Python')
print("""Guido's the ex-"BDFL" of Python""")

# triple quotes:   """xxx"""   '''xxx'''

#  str
s3 = r"spam\n"  # raw string --  \ is not magic  (doesn't escape special character)
print(s3)

person = "Taylor Swift"  # strings are immutable (read-only)
print(f"{person = }")

print(f"{'ayl' in person = }")
print(f"{'Swift' in person = }")
print(f"{'Slow' in person = }")

tu = person.upper()  # upper() is a method of a str object 
print(f"{tu = }")
print(len(person))
print(person.count('t'))
print(person.count('T'))
print(f"{person.lower().count('t') = }")  # method chaining

print(f"{person.endswith('Swift') = }")
print(f"{person.endswith('Slow') = }")

print(f"{person.removeprefix('Taylor') = }")

pos = person.find('lor')
print(f"{pos = }")
print(f"{person.find('wombat') = }")

line = "April:Michigan:22"
fields = line.split(':')
print(f"{fields = }")

phrase = "shake it off"
words = line.split()
print(f"{words = }")

lyric = "     I stay out too late      "
print("|" + lyric + "|")
print("|" + lyric.lstrip() + "|")
print("|" + lyric.rstrip() + "|")
print("|" + lyric.strip() + "|")

raw_amount = "$10,398.22"
amount = raw_amount.replace(',','').lstrip('$')
print(f"{amount = }")

s = "$00005"
print(f"{s.lstrip('0$') = }")











