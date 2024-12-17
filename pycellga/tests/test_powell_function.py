import pytest
from pycellga.problems.single_objective.continuous.powell import Powell

@pytest.fixture
def setup_powell():
    """
    Fixture to provide an instance of the Powell problem with a default number of variables.
    
    Returns
    -------
    Powell
        An instance of the Powell optimization problem.
    """
    return Powell(n_var=8)  # Default number of variables

def test_powell_function(setup_powell):
    """
    Test the Powell function implementation.

    This test verifies the accuracy of the Powell function by evaluating it at predefined
    input points and comparing the results to the expected fitness values.

    Parameters
    ----------
    setup_powell : Powell
        The fixture providing an instance of the Powell problem.

    Test Cases
    ----------
    - [0.0, 0.0, 0.0, 0.0]: Expected result is 0.0.
    - [1.0, 2.0, 3.0, 4.0]: Expected result is 1512.0.
    - [1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0]: Expected result is 3024.0.
    - [5.0, -4.0, 0.0, 0.0, 2.0, -3.0, 4.0, -5.0]: Expected result is 47571.0.
    """
    test_cases = [
        ([0.0, 0.0, 0.0, 0.0], 0.0),
        ([1.0, 2.0, 3.0, 4.0], 1512.0),
        ([1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0], 3024.0),
        ([5.0, -4.0, 0.0, 0.0, 2.0, -3.0, 4.0, -5.0], 47571.0),
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_powell.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float), "Fitness value should be a float."
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-1), \
            f"Expected {expected_fitness}, got {fitness_value}"

if __name__ == "__main__":
    pytest.main()
