from typing import List, Any
from abc import ABC, abstractmethod
from pymoo.core.problem import Problem

from pycellga.common import GeneType

class AbstractProblem(Problem, ABC):
    """
    Abstract base class for defining optimization problems compatible with pymoo.

    This class provides a structure for defining optimization problems, where the
    user specifies the gene type, the number of variables, and their bounds. It includes
    an abstract method `f` for evaluating the fitness of a solution, which must be
    implemented by subclasses.

    Attributes
    ----------
    gen_type : GeneType
        The type of genes used in the problem (e.g., REAL, BINARY).
    n_var : int
        The number of design variables.
    xl : List[float] or numpy.ndarray
        The lower bounds for the design variables.
    xu : List[float] or numpy.ndarray
        The upper bounds for the design variables.

    Methods
    -------
    f(x: List[Any]) -> float
        Abstract method to compute the fitness value for a given solution. 
        Must be implemented by subclasses.
    evaluate(x, out, *args, **kwargs)
        Computes the objective value(s) for pymoo's optimization framework.
    """

    def __init__(self, gen_type: GeneType, n_var, xl, xu):
        """
        Initialize the AbstractProblem with gene type, variable count, and bounds.

        Parameters
        ----------
        gen_type : Any
            The type of genes used in the problem (e.g., REAL, BINARY).
        n_var : int
            The number of design variables.
        xl : float 
            The lower bound for the design variables.
        xu : float
            The upper bound for the design variables.
        """
        self.gen_type = gen_type

        super().__init__(n_var=n_var, n_obj=1, n_constr=0, xl=xl, xu=xu)

    @abstractmethod
    def f(self, x: List[Any]) -> float:
        """
        Abstract method for evaluating the fitness of a solution.

        This method must be implemented by subclasses to define the objective function
        of the optimization problem.

        Parameters
        ----------
        x : list
            List of design variable values.
        
        Returns
        -------
        float
            The computed fitness value for the given solution.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def evaluate(self, x, out, *args, **kwargs):
        """
        Evaluate function for compatibility with pymoo's optimizer.

        This method wraps the `f` method and allows pymoo to handle batch evaluations
        by storing the computed fitness values in the output dictionary.

        Parameters
        ----------
        x : numpy.ndarray
            Array of input variables.
        out : dict
            Dictionary to store the output fitness values.
        """
        out["F"] = self.f(x)
