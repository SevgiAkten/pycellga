from enum import Enum 
from numpy import random
import numpy as np
import random as rd
from problems.abstract_problem import AbstractProblem


class GeneType(Enum):
    """
    GeneType is an enumeration class that represents the type of genome representation for an individual in an evolutionary algorithm.
    The three types of genome representation are BINARY, PERMUTATION, and REAL.
    """
    BINARY = 1
    PERMUTATION = 2
    REAL = 3



class Individual:
    """
    A class to represent an individual in an evolutionary algorithm.

    Attributes
    ----------
    chromosome : list
        The chromosome representing the individual.
    fitness_value : float
        The fitness value of the individual.
    position : tuple
        The position of the individual, represented as a tuple (x, y).
    neighbors_positions : list or None
        The positions of the individual's neighbors.
    neighbors : list or None
        The list of neighbors for the individual.
    gen_type : GeneType
        The enum type of genome representation (GeneType.BINARY, GeneType.PERMUTATION, GeneType.REAL).
    ch_size : int
        The size of the chromosome.
    """

    def __init__(self, 
                 gen_type: GeneType = GeneType.BINARY, 
                 ch_size: int = 0,
                 mins : list[float] = [],
                 maxs : list[float] = []):
        """
        Initialize an Individual with a specific genome type and chromosome size.

        Parameters
        ----------
        gen_type : str, optional
            The type of genome representation. Must be one of GeneType.BINARY, GeneType.PERMUTATION, or GeneType.REAL. (default is GeneType.BINARY)
        ch_size : int
            The size of the chromosome.
        mins: list[float]
            The minimum values for each gene in the chromosome.
        maxs: list[float]
            The maximum values for each gene in the chromosome.

        Description:
        ------------
        The Individual class represents an individual in an evolutionary algorithm.
        If the genome type is BINARY, the chromosome is a list of 0s and 1s.
        If the genome type is PERMUTATION, the chromosome is a list of integers representing a permutation.
        In both the binary and permutation cases, ch_size is enought to represent the chromosome.
        If the genome type is REAL, the chromosome is a list of real numbers.
        In this case, the mins and maxs lists are used to define the range of each gene in the chromosome.
        """
        self.gen_type = gen_type
        self.ch_size = ch_size
        self.chromosome = []
        self.fitness_value = 0
        self.position = (0, 0)
        self.neighbors_positions = None
        self.neighbors = None
        self.mins = mins
        self.maxs = maxs


    def randomize(self):
        """
        Randomly initialize the chromosome based on the genome type.

        Returns
        -------
        list
            The randomly generated chromosome.
        
        Raises
        ------
        NotImplementedError
            If the genome type is not implemented.
        """

        if self.gen_type == GeneType.BINARY:
            self.chromosome = [random.randint(2) for i in range(self.ch_size)]
            
        elif self.gen_type == GeneType.PERMUTATION:
            # Generate a random permutation of the numbers 1 to ch_size.
            # by default random.permutation emits numbers from 0 to ch_size-1
            # so we add 1 to each number to get the desired range.
            self.chromosome = list(np.random.permutation(self.ch_size) + 1)

        elif self.gen_type == GeneType.REAL:
            if len(self.mins) > 0:
                assert len(self.mins) == len(self.maxs) == self.ch_size
                self.chromosome = [rd.uniform(self.mins[i], self.maxs[i]) for i in range(self.ch_size)]
            else:
                self.chromosome = [rd.uniform(-1.0, 0.1) for i in range(self.ch_size)]

        else:
            raise NotImplementedError("This gen_type not implemented yet.")
        return self.chromosome


    def generate_candidate(self, probvector: list) -> list:
        """
        Generate a candidate chromosome based on the given probability vector.

        Parameters
        ----------
        vector : list of float
            The probability vector used to generate the candidate chromosome.

        Returns
        -------
        list
            The generated candidate chromosome as a list of 0s and 1s.
        """
        ind = [1 if random.rand() < p else 0 for p in probvector]
        return ind

    def getneighbors_positions(self) -> list:
        """
        Get the positions of the individual's neighbors.

        Returns
        -------
        list or None
            The positions of the individual's neighbors.
        """
        return self.neighbors_positions

    def setneighbors_positions(self, positions: list) -> None:
        """
        Set the positions of the individual's neighbors.

        Parameters
        ----------
        positions : list
            The positions to set for the individual's neighbors.
        """
        self.neighbors_positions = positions

    def getneighbors(self) -> list:
        """
        Get the list of neighbors for the individual.

        Returns
        -------
        list or None
            The list of neighbors for the individual.
        """
        return self.neighbors

    def setneighbors(self, neighbors: list) -> None:
        """
        Set the list of neighbors for the individual.

        Parameters
        ----------
        neighbors : list
            The list of neighbors to set for the individual.
        """
        self.neighbors = list(neighbors)