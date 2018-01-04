def convert_to_celcius(fahrenheit):
    
    '''(number) -> number

    Return temperature in degree celcius equivalent to degree fahrenheit.

    >>> convert_to_celcius(32)
    0
    >>> convert_to_celcius(212)
    100
    '''
    return (fahrenheit - 32) * 5 / 9
