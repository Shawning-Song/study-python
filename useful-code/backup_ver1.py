__author__ = 'Shawning'

import os
import time


rar_exe = 'rar.exe'

source = [r'./test1', r'./test2']

target_dir = r'./rar_respo'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.rar'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

rar_command = r'{} a {} {}'.format(rar_exe, target, ' '.join(source))

# print(rar_command)

os.system(rar_command)