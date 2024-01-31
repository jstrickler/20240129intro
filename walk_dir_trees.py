import os

START_FOLDER = "."

for curr_dir, dir_list, file_list in os.walk(START_FOLDER):
    if '.git' in dir_list:
        dir_list.remove('.git')
    if 'venv' in dir_list:
        dir_list.remove('venv')
    print(curr_dir)
    for file_name in file_list:
        if file_name.endswith('.py'):
            file_path = os.path.join(curr_dir, file_name)
            # open file_path and read
            file_size = os.path.getsize(file_path)
            print(f"    {file_size:6d} {file_name}")


