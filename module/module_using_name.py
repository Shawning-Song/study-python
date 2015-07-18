__author__ = 'Administrator'

import test1

# 使用__name__属性来判断这个模块是被import执行的
# 还是自己执行的

if __name__ == '__main__':
    print(__name__ + ' 自己执行的')
else:
    print(__name__ + ' 导入执行的.')

for i in dir(test1):
    print('attributions in test1 is {}'.format(i))

help(test1)
print(test1.__test1_version__)