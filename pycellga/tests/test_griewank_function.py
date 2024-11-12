import pytest
from problems.single_objective.continuous.griewank import Griewank

@pytest.fixture
def setup_griewank():
    """
    Fixture for creating an instance of the Griewank problem.

    Returns
    -------
    Griewank
        An instance of the Griewank problem.
    """
    return Griewank(dimensions=2) 

def test_griewank_function(setup_griewank):
    """
    Test the Griewank function implementation.

    This test checks the calculation of the Griewank function value for given lists of float variables.
    It uses predefined inputs and compares the outputs to the expected values.

    Parameters
    ----------
    setup_griewank : fixture
        The fixture providing the Griewank problem instance.
    """
    # Define sample input variables and their expected Griewank function values
    test_cases = [
        ([0.0, 0.0], 0.0),  # Global minimum
        ([600.0, 600.0], 180.012),  # Boundary point
        ([-600.0, -600.0], 180.012),  # Boundary point
        ([100.0, 200.0], 14.361),  # Arbitrary point
        ([-300.0, 300.0], 46.002)  # Another arbitrary point
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_griewank.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}")
        assert isinstance(fitness_value, float), "Fitness value should be a float."
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-3), \
            f"Expected {expected_fitness}, got {fitness_value}"

if __name__ == "__main__":
    pytest.main()
