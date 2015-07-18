__author__ = 'Administrator'
# bad thing:
#'''this is test1 module.''' \
#'''hahaha'''



# define one variable
test1_one = 1

# define one __variable__
__test1_version__ = 1.0

def test1_func1():
    print('test1_func1 is run.')





if __name__ == '__main__':
    print(__name__ + ' 自己执行的')
else:
    print(__name__ + ' 导入执行的.')