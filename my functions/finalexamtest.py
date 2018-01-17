def f(x):
    y = x * 3
    return y - x

start = 'L'
middle = 8
end = 'R'
'''Write an expression that evaluates to the string 'L8R' using only
the variables start, middle, end, one call on function str, and string
concatenation.'''
start + str(middle) + end

def count_max_letters(s1, s2, letter):
    '''(str, str, str) -> int 

    s1 and s2 are strings, and letter is a string of length 1.
    Count how manytimes letter appears in s1 and in s2, and return the
    bigger of the twocounts.

    >>> count_max_letters('hello', 'world', 'l')
    2
    >>> count_max_letters('cat', 'abracadabra', 'a')
    5
    '''

    '''The expression for the return statement is missing. Write that
    expression below. Use only the parameters, one call on function max, and
    two calls on str method count. Do not use unnecessary parentheses:
    you need them for the function and method calls, but nothing else.
    Do not include the word return; just write the expression.'''
    
    # CODE MISSING HERE
    return max(s1.count(letter),s2.count(letter))


def same_length(L1, L2):
    '''(list, list) -> bool

    Return True if and only if L1 and L2 contain the same number of elements.
    '''

    '''if len(L1) == len(L2):
       return True
    else:
       return False'''
    # The function works, but the if statement can be replaced with a single return statement:
    # Write the missing expression. Use only the parameters, two calls on function len, and operator == once.
    return len(L1)==len(L2)

# 7.Consider these two functions; we provide only the headers, type contracts, and a precondition:
def burble(a, b):
    '''(int, float) -> str'''
def snorgle(L):
    '''(list of str) -> float
    Precondition: L has at least one element.'''
'''Below are code fragments that call these two functions in various ways.
Select the code fragment(s) below that are valid according to the function
headers and the type contracts.'''
# snorgle([burble(1, 1.0), 'b'])
# burble(len(burble(1, 2.2)), 3.3)


#8.
def gather_every_nth(L, n):
    '''(list, int) -> list

    Return a new list containing every n'th element in L, starting at index 0.

    Precondition: n >= 1

    >>> gather_every_nth([0, 1, 2, 3, 4, 5], 3)

    [0, 3]
    >>> gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2)
    ['a', 'c', 'e', 'g', 'i']
    '''
    '''Write the missing expression. Do not use parentheses. Do not include "i =". Just write the missing expression.'''
    
    result = []
    i = 0
    while i < len(L):
        result.append(L[i])
        i = i + n
   
    return result

# 9.
def get_keys(L, d):
    '''(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    [1, 'a']
    '''
    '''Write the missing code for the first line of the for loop — everything
    after the word "for", up to and including the colon :.
    Do not use any parentheses, and do not call any functions or methods.
    '''
    result = []
    for k in L:
       if k in d:
          result.append(k)

    return result

# 10.
def are_lengths_of_strs(L1, L2):
    '''(list of int, list of str) -> bool
  
    Return True if and only if all the ints in L1 are the lengths of the strings
    in L2 at the corresponding positions.

    Precondition: len(L1) == len(L2)

    >>> are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef'])
    True
    '''
    '''Write the missing code for the if statement — everything after the
    word "if", up to and including the colon :.
    Your answer should be of the form expr1 != expr2:, where expr1 and
    expr2 are expressions. Use only variables i, L1, L2, indexing, and
    function len.
    Do not use parentheses except for the call on len.'''
    result = True
    for i in range(len(L1)):
        if L1[i] != len(L2[i]):
            result = False

    return result

# 11.
def double_last_value(L):
    '''(list of int) -> NoneType

    Double the value at L[-1]. For example, if L[-1] is 3,
    replace it with 6.

    Precondition: len(L) >= 1.
    '''
    # And this code:
L1 = [1, 3, 5]
double_last_value(L1)
print(L1[-1])

#Enter the number that gets printed.
#10

# 12.
def get_negative_nonnegative_lists(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the negative ints in the
    inner lists of L and the second item is a list of the non-negative ints
    in those inner lists.

    Precondition: the number of rows in L is the same as the number of
    columns.

    >>> get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]])
    ([-1, -4], [3, 5, 2, 5, 4, 0, 8])
    '''

    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
            # Select the code fragment(s) that correctly complete this function.
            # CODE MISSING HERE
            '''val = L[row][col]
            if val < 0:
                neg.append(val)
            else:
                nonneg.append(val)'''
            if L[row][col] < 0:
                neg.append(L[row][col])
            else:
                nonneg.append(L[row][col])


    return (neg, nonneg)

# 13.
def count_chars(s):
    '''(str) -> dict of {str: int}

    Return a dictionary where the keys are the characters in s and the values
    are how many times those characters appear in s.

    >>> count_chars('abracadabra')
    {'a': 5, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
    '''
    d = {}

    for c in s:
        if not (c in d):
            # Write the missing assignment statement. Do not call any
            # functions or methods. Do not use unnecessary parentheses.
            # CODE MISSING HERE
            d[c] = 1
        else:
            d[c] = d[c] + 1

    return d
