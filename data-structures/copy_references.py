__author__ = 'Shawning'


showlist = ['apple', 'mango', 'carrot', 'banana']

reference_showlist = showlist

print('before delete:', showlist)
del showlist[0]

print('showlist:', showlist)
print('reference_showlist:', reference_showlist)

copy_list = showlist[:]
del showlist[0]
print('showlist:', showlist)
print('copy_list:', copy_list)