
__author__ = 'Shawning'


import os
import time

rar_exe = 'rar.exe'

source = [r'./test1', r'./test2']

target_dir = r'./rar_respo'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

print(today)
print(now)

# comment = raw_input

target = today + os.sep + now + '.rar'

if not os.path.exists(today):
    os.mkdir(today)

rar_command = r'{} a {} {}'.format(rar_exe, target, ' '.join(source))

os.system(rar_command)