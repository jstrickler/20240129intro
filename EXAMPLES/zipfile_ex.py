
from zipfile import ZipFile, ZIP_DEFLATED
import os.path

# reading & extracting from zip file
zip_in = ZipFile("../DATA/textfiles.zip")  # Open zip file for reading
print(zip_in.namelist())  # Print list of members in zip file
tyger_text = zip_in.read('tyger.txt').decode()  # Read (raw binary) data from member and convert from bytes to string
print(tyger_text[:100], '\n')
zip_in.extract('parrot.txt')  # Extract member

# creating a zip file
file_names = ["parrot.txt", "tyger.txt", "knights.txt", "alice.txt", "poe_sonnet.txt", "spam.txt"]
zip_out = ZipFile("example.zip", mode="w", compression=ZIP_DEFLATED)  # Create new zip file
for file_name in file_names:
    file_path = os.path.join("../DATA", file_name)
    print("adding {}".format(file_path))
    zip_out.write(file_path, file_name)  # Add member to zip file
