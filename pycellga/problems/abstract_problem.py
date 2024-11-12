from abc import ABC, abstractmethod
from typing import List, Tuple, Union, Any
from pymoo.core.problem import Problem

class AbstractProblem(Problem, ABC):
    """
    Abstract base class for optimization problems.
    """

    def __init__(self, 
                 design_variables: Union[int, List[str]], 
                 bounds: List[Tuple[float, float]], 
                 objectives: Union[str, int, List[str]], 
                 constraints: Union[str, int, List[str]] = []):
        """
        Initialize the problem with variables, bounds, objectives, and constraints.
        
        Parameters
        ----------
        design_variables : int or List[str]
            If an integer, it specifies the number of design variables. 
            If a list of strings, it specifies the names of design variables.
        bounds : List[Tuple[float, float]]
            Bounds for each design variable as (min, max).
        objectives : str, int, or List[str]
            Objectives for optimization, e.g., "minimize" or "maximize".
        constraints : str, int, or List[str], optional
            Constraints for the problem (default is an empty list).
        """
        # Ensure objectives and constraints are always lists
        objectives = [str(objectives)] if isinstance(objectives, (str, int)) else list(objectives)
        constraints = [str(constraints)] if isinstance(constraints, (str, int)) else list(constraints)

        # Pymoo-specific attributes
        n_var = design_variables if isinstance(design_variables, int) else len(design_variables)
        xl = [bound[0] for bound in bounds]
        xu = [bound[1] for bound in bounds]
        
        super().__init__(n_var=n_var, n_obj=len(objectives), n_constr=len(constraints), xl=xl, xu=xu)
        
        # Custom attributes
        self.design_variables = [f"x{i+1}" for i in range(n_var)] if isinstance(design_variables, int) else design_variables
        self.bounds = bounds
        self.objectives = objectives
        self.constraints = constraints

    @abstractmethod
    def f(self, x: List[Any]) -> float:
        """
        Abstract method for evaluating the fitness of a solution.
        
        Parameters
        ----------
        x : list
            List of design variable values.
        
        Returns
        -------
        float
            Fitness value.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def evaluate(self, x, out, *args, **kwargs):
        """
        Evaluate function for compatibility with pymoo's optimizer.
        
        Parameters
        ----------
        x : numpy.ndarray
            Array of input variables.
        out : dict
            Dictionary to store the output fitness values.
        """
        out["F"] = self.f(x)
