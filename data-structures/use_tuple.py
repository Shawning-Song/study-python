__author__ = 'Shawning'


zoo = ('one', 'two', 'three')
print('Number of animals in the zoo is {}'.format(len(zoo)))
print('Number of animals in the zoo is', len(zoo))


new_zoo = ('four', 'five', zoo)
print('Numer of cages in the new zoo is {}'.format(len(new_zoo)))

print('All animals in newe zoo are:', new_zoo)

for i in new_zoo:
    print(i)


# define an empty tuple
tuple_empty = ()
print(tuple_empty)

# define a tuple with only one item
# error: tuple_with_one = ('one')
tuple_with_one = ('one', )
print(tuple_with_one)
