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
    count = 0
    for ntype in dna:
        if ntype == nucleotide:
            count += 1
    return count


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
    """ (str) -> bool

    Return True if sequence is valid sequance of characters 
    representing DNA. All letters must be UPPERCASE to be valid
    
    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ACGTAB')
    False
    
    """
    valid = True
    for ntype in dna:
        if ntype not in 'ATGC':
            valid = False
    return valid

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str
​    Return the DNA sequence obtained by inserting 
    the second DNA sequence into the first DNA sequence 
    at the given index.

    >>> insert_sequence("AAAA", "ATGC", 1)
    'AATGCAAA'
    >>> insert_sequence('ATGC', 'GAAAATTTCC', 5)
    """
    return dna1[:index]+dna2+dna1[index:]
 	
def get_complement(nucleotide):
    """ (str) - > str
    Return the nucleotide's complement for the given nucleotide

    >>> get_complement("A")
    'T'
    >>> get_complement("C")
    'G'
    """
    if nucleotide not in "ATCG":
        print('Incorrect nucleotide type')
    else:
        if nucleotide == "A":
            return "T"
        elif nucleotide == "T":
            return "A"
        elif nucleotide =="C":
            return "G"
        else:
            return "C"

def get_complementary_sequence(dna):
    """ (str) -> str
    Return the DNA sequence that is complementary to the given DNA sequence.
    >>> get_complementary_sequence("ACGTACG")
    "TGCATGC"
    >>> get_complementary_sequence("AAGGGCATT")
    "TTCCCGTAA"
    """
    complementary_dna = ""
    for ntype in dna:
        if ntype == "A":
            ntype = "T"
            complementary_dna +=ntype
        elif ntype == "T":
            ntype = "A"
            complementary_dna +=ntype
        elif ntype == "G":
            ntype = "C"
            complementary_dna +=ntype
        else:
            ntype = "G"
            complementary_dna +=ntype
    return complementary_dna
   