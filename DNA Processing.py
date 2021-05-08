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
    nuc = ''
    for ch in dna:
        if ch in nucleotide:
            nuc = nuc + ch

    return len(nuc)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna2 in dna1:
        return True
    else:
        return False

def is_valid_sequence(dna):
    '''
    (str) -> bool
    Return True if and only if the return value is valid(that is it should not contain values other than 'A' 'G' 'T' 'C')

    >>>is_invalid_sequence("ATCG")
    True
    >>>is_invalid_sequence("DFGHJK")
    False

    '''

    for ch in dna:
        if ch in ('ATCG'):
            return True
        else:
            return False

def insert_sequence(dna1, dna2, index):
    '''
    (str, str, int) -> str
    Return the DNA sequence obtained by inserting the second DNA sequence into
    the first DNA sequence at the given index.

    >>>insert_sequence('CCGG', 'AA', 2)
    CCAAGG
    >>>insert_sequence('ATKT', 'TT', 1)
    ATTTKT
    '''
    return dna1[:index] + dna2 + dna1[index:]

def get_complement(nucleotide):
    '''

    (str) -> str
    Return the nucleotide's complement.

    >>>get_complement('A')
    T
    >>>get_complement('C')
    G
    '''
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
         return 'A'

    if nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
            return 'C'

def get_complementary_sequence(dna):
    '''
    (str) -> str

    Return the complement of a given DNA sequence.

    >>> get_complementary_sequence('ATCGGACT')
    TAGCCTGA
    >>> get_complementary_sequence('GCACTCC')
    CGTGAGG
    '''
    c = ''
    for ch in dna:
        c = c + get_complement(ch)
    return c
