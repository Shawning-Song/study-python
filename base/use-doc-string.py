__author__ = 'Administrator'


# use doc string
def use_doc_string():
    '''this is study.''' \
    '''\nsecond line.'''
    print('use doc string')

def use_doc_string2():
    '''hahahaha
    hahahaha'''




print(use_doc_string.__doc__)
print(use_doc_string2.__doc__)