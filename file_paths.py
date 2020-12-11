import os   # os.path
from datetime import datetime

FOLDER = 'DATA'

FILE_NAME = 'alice.txt'

file_path = os.path.join(FOLDER, FILE_NAME)

with open(file_path) as alice_in:    # DATA/alice.txt  DATA\alice.txt
    pass

file_size = os.path.getsize(file_path)
print("file_size: {}\n".format(file_size))

print(os.path.dirname(file_path))
print(os.path.basename(file_path))

print(os.path.abspath(file_path))

for x in 'alice.txt', 'parrot.txt', 'wombat.txt', 'windows.hate':
    x_path = os.path.join(FOLDER, x)
    print(x_path, os.path.exists(x_path))
print()

raw_ts = os.path.getmtime(file_path)
print("raw timestamp:", raw_ts)

file_ts = datetime.fromtimestamp(raw_ts)
print("file mod timestamp:", file_ts)

raw_access_ts = os.path.getatime(file_path)
file_access_ts = datetime.fromtimestamp(raw_access_ts)
print("file access timestamp:", file_access_ts)
print()

all_items = os.listdir('ANSWERS')
print(all_items)
print()






