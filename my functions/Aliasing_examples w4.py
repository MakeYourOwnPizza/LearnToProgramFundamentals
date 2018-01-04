list1 = [0,2,4,6,8,10]
list2 = list1
list1[-1] = 17
print(list1[-1])
print(list2[-1])


def double_even_indices(lst):
    '''(list of int) -> NoneType
    
    Double every other int in lst, starting at index 0.
    '''
    
    i = 0
    while i < len(lst):
        lst[i] = lst[i] * 2
        i = i + 2
        
list1 = [11, 12, 13, 14, 15, 16, 17]
print(list1)
double_even_indices(list1)
print(list1)


def print_every_third_char(s):
    for i in range(0, len(s), 3):
        print(s[i])

def mystery(s):
    i = 0
    result = ''

    while not s[i].isdigit():
          result = result + s[i]
          i = i + 1

    return result
