from pip._vendor.distlib.compat import raw_input

number = 23
guess = int(raw_input('Enter an integer: '))

if guess == number:
    print('one.py: good')
elif guess < number:
    print('one.py: smaller')
else:
    print('one.py: bigger')

print('one.py: done')