import os

start_dir = "."
start_dir = os.path.abspath(start_dir)

for dirname, dirs, files in os.walk(start_dir):
    if '.git' in dirs:
        dirs.remove('.git')
    print(dirname)
    for file_name in files:
        if file_name.startswith('s') and file_name.endswith('.py'):
            file_path = os.path.join(dirname, file_name)
            file_size = os.path.getsize(file_path)
            print("\t{:5d} {}".format(file_size, file_path))



