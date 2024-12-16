from enum import Enum 

class GeneType(Enum):
    """
    GeneType is an enumeration class that represents the type of genome representation for an individual in an evolutionary algorithm.
    The three types of genome representation are BINARY, PERMUTATION, and REAL.
    """
    BINARY = 1
    PERMUTATION = 2
    REAL = 3