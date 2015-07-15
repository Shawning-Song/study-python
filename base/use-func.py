__author__ = 'Administrator'


# practice define some functions

# easy
def say_hello():
    print('Hello World.')

# take some parameters
def print_max(a, b):
    if a > b:
        print('a is bigger.')
    elif a < b:
        print('b is bigger.')
    else:
        print('a == b.')

# local variables
global_number = 100

def print_local(global_number):
    print('number is {}.' .format(global_number))
    global_number = 10
    print('number is {}.' .format(global_number))

def print_global():
    print('global is {}' .format(global_number))

say_hello()
print_max(3, 4)
print_local(global_number)
print(global_number)
print_global()