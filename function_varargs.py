__author__ = 'Administrator'


# function with variable number of arguments
# *numbers is tuple
# **keywords is dictionary

def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number

    for key in keywords:
        count += keywords[key]

    return count

print(total(1, 1, 1, 1, a=2, b=2))
