import os
from datetime import datetime

FOLDER = "DATA"
FILE_NAME = "alice.txt"

file_path = os.path.join(FOLDER, FILE_NAME)
print(f"{file_path = }")

base_name = os.path.basename(file_path)
print(f"{base_name = }")

dir_name = os.path.dirname(file_path)
print(f"{dir_name = }")

abs_path = os.path.abspath(file_path)
print(f"{abs_path = }")

base_name, dir_name = os.path.split(file_path)
print(f"{base_name = }")
print(f"{dir_name = }")

path, ext = os.path.splitext(file_path)
print(f"{path = }")
print(f"{ext = }")

drive, path = os.path.splitdrive(abs_path)
print(f"{drive = }")
print(f"{path = }")

file_size = os.path.getsize(file_path)
print(f"{file_size = }")

raw_ts = os.path.getmtime(file_path)
print(f"{raw_ts = }")
file_ts = datetime.fromtimestamp(raw_ts)  # be sure to import datetime from datetime
print(f"{file_ts = }")
