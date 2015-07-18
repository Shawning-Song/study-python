__author__ = 'Shawning'


def cmp_numer(a, b):
    return a>b


list1 = [];

print(list1)

list1.append(1)
list1.append(2)
print(list1)
list1[1] = 10
print(list1)

list1.append(4)
list1.append(100)
list1.append(88)
#list1[2] = 3



print('before sort:')
print(list1)
list1.sort()
print('after sort  smaller->bigger:')
print(list1)
# todo: study sort function
# list1.sort(cmp_numer)
# print('after sort  bigger->smaller:')
# print(list1)
print('I have', len(list1), 'items.')