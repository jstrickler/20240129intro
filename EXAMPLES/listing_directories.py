import os

DIRECTORY = '../DATA'

for entry_name in os.listdir(DIRECTORY)[:9]:
    print(entry_name)
print('-' * 60)

for i, entry in enumerate(os.scandir(DIRECTORY)):
    print("{:25s} {:6s} {:6s} {:6o}".format(entry.name, str(entry.is_dir()), str(entry.is_file()), entry.stat().st_mode))
    if i == 9:
        break
