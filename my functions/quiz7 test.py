def eat(d):
    '''(dict of {str: int}) -> bool

    Each key in d is a fruit and each value is the quantity of     that fruit.

    REST OF DESCRIPTION MISSING HERE
    Remove from d all fruits that have a value of 0 associated with them and
    return True if and only if the were no such fruits.
    
    >>> eat({'apple': 2, 'banana': 3, 'pear': 3, 'peach': 1})
    True
    >>> eat({'apple': 0, 'banana': 0})
    False
    '''
    ate = False
    for fruit in d:
        if d[fruit] > 0:
            d[fruit] = d[fruit] - 1
            ate = True

    return ate

def contains(v, d):
    ''' (object, dict of {object: list}) -> bool

    Return whether v is an element of one of the list values in d.
    >>> contains('moogah', {1: [70, 'blue'], 2: [1.24, 'moogah', 90], 3.14: [80, 100]})
    True
    >>> contains('moogah', {'moogah': [1.24, 'frooble', 90], 3.14: [80, 100]})
    False
    '''

    found = False # Whether we have found v in a list in d.

    # CODE MISSING HERE, 2 choices below
    '''for k in d:
        if v in d[k]:
            found = True'''

    for k in d:
        for i in range(len(d[k])):
            if d[k][i] == v:
                found = True
 
    return found

def count(dictionary):
    '''L = []
    for k in d:
        L.extend(d[k])

    total = len(L)'''
    total = 0
    for k in d:
        total = total + len(d[k])

    return total

L = [['apple', 3], ['pear', 2], ['banana', 3]]
d = {}
for item in L:
   d[item[0]] = item[1]
