import sys
import platform

print(sys.argv, '\n')

print(sys.platform, '\n')  # win32=Windows  linux=Linux  darwin=Mac

print(sys.prefix, '\n')

print(sys.executable, '\n')

print(sys.version, '\n')

print(sys.version_info, sys.version_info.major, '\n')

m = sys.modules

import re

print(m['re'])

import os
def get_distro():
    distro_id = 'NOT FOUND'
    for file_path in '/etc/lsb-version', '/etc/os-version':
        if os.path.exists(file_path):
            with open(file_path) as distro_id_in:
                distro_id = distro_id_in.read().rstrip()
    return distro_id

