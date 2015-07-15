__author__ = 'Administrator'


# define global variables
global_variables = 100

# define function to change and print the global_variables
def change_print_global():
    # declare the global variables
    global global_variables
    print('global is {}'.format(global_variables))
    global_variables = 10
    print('change global is {}'.format(global_variables))

# call the function
change_print_global()

# print the global out of the function
print('Value of global_variables is {}'.format(global_variables))

format_str = '{} is {}'
after_str = format_str.format(global_variables, global_variables)
print(after_str)
