def shift_left(L):
    ''' (list) -> NoneType (the function modifies the list, so it's NoneType)

    Shift each item in L one position to the left
    and shift the first item to the last position.

    Precondition: len(L) >= 1

    >>> sev = [7]
    >>> shift_left(sev)
    >>> sev
    [7]
    '''

    first_item = L[0]

    for i in range(1, len(L)):
        L[i - 1] = L[i]
        
    L[-1] = first_item
    return L
    
def count_adjacent_repeats(s):
    '''(str) -> int

    Return the number of occurrences of a chracter and
    an adjacent character being the same.
    
    >>>count_adjacent_repeats('abccdeffggh')
    3
    '''

    repeats = 0

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            repeats = repeats + 1
    return repeats
