def get_anwer(prompt):
    '''(str) -> str

    Use prompt to ask the user for a "yes" or "no"
    answer and continue aksing until the user gives
    a valid response. Return the answer.
    '''

    answer = input(prompt)

    while not (answer == 'yes' or answer == 'no'):
        answer = input(prompt)

    return answer

def up_to_vowel(s):
    '''(str) -> str

    Return a substring of s from index 0 up to but
    not including the first vowel in s.

    >>>up_to_vowel('hello')
    'h'
    >>>up_to_vowel('there')
    'th'
    >>>up_to_vowel('cs')
    'cs'
    '''
    # before_vowel contains all the characters found in s[0:i].
    before_vowel = ''
    i = 0

    # Accumulate the non-vowels at the beginning of the string.
    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        before_vowel = before_vowel + s[i]
        i = i + 1

    return before_vowel

def even_numbers_sum(num1, num2):
    '''(int, int) -> int

    Return the sum of the even or odd numbers from num1 through num2(inclusive).
    
    >>> even_numbers_sum(2,10)
    30
    >>> even_numbers_sum(4,20)
    108
    '''

    num = num1
    sum = num1
    
    while num < num2:
        num = num + 2 
        sum = sum + num
    return sum

def even_numbers_sum2(num1, num2):
    '''(int, int) -> int

    Return the sum of the even or odd numbers from num1 through num2(inclusive).
    
    >>> even_numbers_sum2(2,10)
    30
    >>> even_numbers_sum2(4,20)
    108
    '''
    sum = 0
    for i in range (num1, num2+2, 2):
        sum = sum + i

    return sum

def while_version(L):
    """ (list of number) -> number
    The while loop stops as soon as an even number is found,
    and the sum of all the previous numbers is returned.
    """
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
        total = total + L[i]
        i = i + 1

    return total

def for_version(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0 and not found_even:
            total = total + num
        else:
            found_even = True
 
    return total

def cap_song_repetition(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.
    >>> cap_song_repetition2(['Lola', 'Venus', 'Lola', 'Lola', 'Let It Be', 'Lola', 'ABC', 'Cecilia', 'Lola', 'Lola'], 'Lola')
    ['Venus', 'Let It Be', 'ABC', 'Cecilia', 'Lola', 'Lola']
    '''
    while playlist.count(song) > 3:
        playlist.remove(song)
    return playlist

def cap_song_repetition2(playlist, song):
    '''(list of str, str) -> NoneType

    Make sure there are no more than 3 occurrences of song in playlist.

    '''
    while playlist.count(song) > 3:
        playlist.remove(playlist.index(song))
    return playlist

def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1

values = [1, 2, 3]
print(increment_items(values, 2))
print(values)

values = []
for num in range(3, 10, 3):
    values.append(num)
print(values)

values = []
for num in range(1, 4):
    values.append(num * 3)
print(values)
