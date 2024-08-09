class AbstractProblem:
    """
    An abstract base class for optimization problems.

    Methods
    -------
    f(x)
        Evaluates the fitness of a given solution x.
    """

    def f(self, x):
        """
        Evaluate the fitness of a given solution x.

        Parameters
        ----------
        x : list
            A list representing a candidate solution.

        Returns
        -------
        float
            The fitness value of the candidate solution.

        Raises
        ------
        NotImplementedError
            If the method is not implemented by a subclass.
        """
        raise NotImplementedError()
