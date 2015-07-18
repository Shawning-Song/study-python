__author__ = 'Administrator'

# import 'sys' module
import sys

print('入参是：')
for i in sys.argv:
    print(i)

# print the python path
print('the PYTHONPATH is {}'.format(sys.path))

path_str = sys.path
for j in path_str:
    print(j)

# the from ... import statement
# 不用使用sys前缀就可以访问argv
from sys import argv
print('xxxx:')
for i in argv:
    print(i)