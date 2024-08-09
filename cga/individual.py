from numpy import random
import random as rd
import numpy as np


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
    gen_type : str
        The type of genome representation ("Binary", "Permutation", "Real-valued").
    ch_size : int
        The size of the chromosome.
    """

    def __init__(self, gen_type="Binary", ch_size=0):
        """
        Initialize an Individual with a specific genome type and chromosome size.

        Parameters
        ----------
        gen_type : str, optional
            The type of genome representation. Must be one of "Binary", "Permutation", or "Real". (default is "Binary")
        ch_size : int
            The size of the chromosome.
        """
        if not gen_type in ["Binary", "Permutation", "Real"]:
            raise ValueError("Invalid genome type. Must be one of 'Binary', 'Permutation', or 'Real'.")
        self.gen_type = gen_type
        self.ch_size = ch_size
        self.chromosome = []
        self.fitness_value = 0
        self.position = (0, 0)
        self.neighbors_positions = None
        self.neighbors = None

    def randomize(self, mins = [], maxs = []):
        """
        Randomly initialize the chromosome based on the genome type.

        Returns
        -------
        Function mutates the original chromosome of the individual and returns it.
        
        Raises
        ------
        NotImplementedError
            If the genome type is not implemented.
        """
        if self.gen_type == "Binary":
            # # CountSat, Fms, Mmdp, OneMax, Ecc, Maxcut20_01, Maxcut20_09, Maxcut100
            self.chromosome = [random.randint(2) for i in range(self.ch_size)]

            
        elif self.gen_type == "Permutation":
            # The random.permutation permutes from 0 to n - 1, however
            # the library requires permutations 1 to n by design. That's why
            # we add 1 to all values.
            self.chromosome = list(np.random.permutation(self.ch_size) + 1)

        elif self.gen_type == "Real":
            # when the genome type is Real, the chrosomes should be initialized 
            # by using given range of values, possibly using arguments.
            # If arguments are not passed, the range is assumed to be [-1, 1].
            if len(mins) == 0:
                self.chromosome = [rd.uniform(-1, 1) for i in range(self.ch_size)]
            else:
                assert len(mins) == len(maxs) == self.ch_size
                self.chromosome = [rd.uniform(mins[i], maxs[i]) for i in range(self.ch_size)]
            

        else:
            raise NotImplementedError(self.gen_type + " not implemented yet.")
        return self.chromosome


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