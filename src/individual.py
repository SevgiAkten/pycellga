from numpy import random
import random as rd
from problems.abstract_problem import AbstractProblem



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

    def __init__(self, 
                 gen_type: str = "", 
                 ch_size: int = 0,
                 problem: AbstractProblem = None):
        """
        Initialize an Individual with a specific genome type and chromosome size.

        Parameters
        ----------
        gen_type : str, optional
            The type of genome representation. Must be one of "Binary", "Permutation", or "Real-valued". (default is "Binary")
        ch_size : int
            The size of the chromosome.
        """
        self.gen_type = gen_type
        self.ch_size = ch_size
        self.problem = problem
        self.chromosome = []
        self.fitness_value = 0
        self.position = (0, 0)
        self.neighbors_positions = None
        self.neighbors = None


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
        problem_name = self.problem.__class__.__name__

        if self.gen_type == "Binary":

            # CountSat, Fms, Mmdp, OneMax, Ecc, Maxcut20_01, Maxcut20_09, Maxcut100
            if problem_name in ["CountSat", "Fms", "Mmdp", "OneMax", "Ecc", "Maxcut20_01", "Maxcut20_09", "Maxcut100"]:
                self.chromosome = [random.randint(2) for i in range(self.ch_size)]
            # Peak
            elif problem_name == "Peak":
                self.chromosome = [[random.randint(2) for g in range(self.ch_size)] for h in range(self.ch_size)]

        elif self.gen_type == "Permutation":

            # Tsp
            if problem_name == "Tsp":
                self.chromosome = list(rd.sample(range(1, 15), self.ch_size))

        elif self.gen_type == "Real-valued":

            # Ackley
            if problem_name == "Ackley":
                self.chromosome = [round(rd.uniform(-32.768, 32.768), 3) for i in range(self.ch_size)]

            # Bohachevsky
            elif problem_name == "Bohachevsky":
                self.chromosome = [random.randint(-15.0, 16.0)for i in range(self.ch_size)]

            # Fms
            elif problem_name == "Fms":
                self.chromosome = [round(rd.uniform(-6.4, 6.35), 3) for i in range(self.ch_size)]

            # Griewank
            elif problem_name == "Griewank":               
                self.chromosome = [round(rd.uniform(-600, 600), 3) for i in range(self.ch_size)]

            # Rastrigin
            elif problem_name == "Rastrigin":                               
                self.chromosome = [round(rd.uniform(-5.12, 5.13), 2) for i in range(self.ch_size)]

            # Rosenbrock
            elif problem_name == "Rosenbrock":                                              
                self.chromosome = [random.randint(-5.0, 11.0) for i in range(self.ch_size)]

            # Schaffer and Schaffer2, Bentcigar, Rothellipsoid
            elif problem_name in ["Schaffer", "Schaffer2", "Bentcigar", "Rothellipsoid"]:
                self.chromosome = [round(rd.uniform(-100, 100), 3) for i in range(self.ch_size)]

            # Matyas, Sumofdifferentpowers
            elif problem_name in ["Matyas", "Sumofdifferentpowers", "Holzman"]:                                            
                self.chromosome = [round(rd.uniform(-10.0, 10.0), 3) for i in range(self.ch_size)]

            # Powell
            elif problem_name == "Powell":                                              
                self.chromosome = [round(rd.uniform(-4.0, 5.0), 3) for i in range(self.ch_size)]

            # Chichinadze
            elif problem_name == "Chichinadze":                                              
                self.chromosome = [round(rd.uniform(-30, 30), 5) for i in range(self.ch_size)]

            # Levy
            elif problem_name == "Levy":                                              
                self.chromosome = [round(rd.uniform(-10.0, 10.0), 2) for i in range(self.ch_size)]

            # Zettle
            elif problem_name == "Zettle":                                              
                self.chromosome = [round(rd.uniform(-5.0, 5.0), 4) for i in range(self.ch_size)]

            # Dropwave, Sphere
            elif problem_name in ["Dropwave", "Sphere"]:                                            
                self.chromosome = [round(rd.uniform(-5.12, 5.12), 3) for i in range(self.ch_size)]

            # # StyblinskiTang
            elif problem_name == "StyblinskiTang":                                             
                self.chromosome = [round(rd.uniform(-5.0, 5.0), 6) for i in range(self.ch_size)]
            
            # # Threehumps
            elif problem_name == "Threehumps":                                             
                self.chromosome = [round(rd.uniform(-5.0, 5.0), 3) for i in range(self.ch_size)]

            # # Zakharov
            elif problem_name == "Zakharov":                                             
                self.chromosome = [round(rd.uniform(-5.0, 10.0), 3) for i in range(self.ch_size)]

            # # Schwefel
            elif problem_name == "Schwefel":                                             
                self.chromosome = [round(rd.uniform(-500.0, 500.0), 3) for i in range(self.ch_size)]

            # # Pow
            elif problem_name == "Pow":                                                            
                self.chromosome = [round(rd.uniform(-5.0, 15.0), 2) for i in range(self.ch_size)]

        else:
            raise NotImplementedError(self.gen_type + " not implemented yet.")
        return self.chromosome

    def generate_candidate(self, vector: list) -> list:
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
        ind = [1 if random.rand() < p else 0 for p in vector]
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