def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1) > len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    '''thenucleotide = 0
    for char in dna:
        if char in nucleotide:
            thenucleotide = thenucleotide + 1
    return thenucleotide'''

    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1

def is_valid_sequence(dna):
    '''(str) -> bool

    Return True if and only if the DNA sequence is valid (that is,
    it contains no characters other than 'A', 'T', 'C' and 'G').
    
    >>>is_valid_sequence('ATOHGC')
    False
    >>>is_valid_sequence('ATCGGC')
    Truen
    '''

    non_nucleotide = 0
    for char in dna:
        if char not in 'ATCG':
            non_nucleotide = non_nucleotide + 1
    return non_nucleotide <= 0 

def insert_sequence(dna1, dna2, position):
    '''(str, str, int) -> str

    Return the DNA sequence obtained by inserting the second
    DNA sequence into the first DNA sequence at the given index.

    Precondition: the index is valid. The index should be greater than 0,
    and smaller than or equal to the length of dna1.
    
    >>>insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>>insert_sequence('CCGG', 'AT', 4)
    'CCGGAT'
    '''

    return dna1[:position] + dna2 + dna1[position:]

def get_complement(nucleotide):
    '''(str) -> str

    Return the nucleotide's complement.
    
    >>>get_complement('A')
    'T'
    >>>get_complement('C')
    'G'
    '''

    if nucleotide == 'A':
        complement_nucleotide = 'T'
    elif nucleotide == 'T':
        complement_nucleotide = 'A'
    elif nucleotide == 'C':
        complement_nucleotide = 'G'
    elif nucleotide == 'G':
        complement_nucleotide = 'C'
    return complement_nucleotide

def get_complementary_sequence(dna):

    '''(str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence.
    
    >>>get_complementary_sequence('ATCGGC')
    'TAGCCG'
    >>>get_complementary_sequence('ACGTACG')
    'TGCATGC'
    '''

    complement_dna = ''
    for char in dna:
        if char == 'A':
            complement_nucleotide = 'T'
            complement_dna = complement_dna + complement_nucleotide
        elif char == 'T':
            complement_nucleotide = 'A'
            complement_dna = complement_dna + complement_nucleotide
        elif char == 'C':
            complement_nucleotide = 'G'
            complement_dna = complement_dna + complement_nucleotide
        elif char == 'G':
            complement_nucleotide = 'C'
            complement_dna = complement_dna + complement_nucleotide
    return complement_dna
