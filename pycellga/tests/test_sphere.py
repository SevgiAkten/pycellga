import pytest
from problems.single_objective.continuous.sphere import Sphere

@pytest.fixture
def setup_sphere():
    """
    Fixture to provide an instance of the Sphere problem.
    """
    return Sphere(design_variables=10)  

def test_sphere(setup_sphere):
    """
    Test the Sphere function implementation.

    This test checks the calculation of the Sphere function value for given input values.

    The Sphere function is a common benchmark function in optimization, where the global minimum is 
    at f(0, 0, ..., 0) = 0. This test ensures that the function computes the correct results for specific
    input values and verifies that the function behaves as expected.

    Parameters
    ----------
    setup_sphere : fixture
        The fixture providing the Sphere problem instance.

    Examples
    --------
    >>> test_sphere()
    """

    # Test cases with exactly 10 variables each, padded with zeros to meet the required length
    test_cases = [
        ([2.305, -4.025, 3.805, -1.505, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 38.256),
        ([-4.995, -2.230, -3.706, 2.305, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 48.970),
        ([0.0 for _ in range(10)], 0.0)  # All zeros, global minimum
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_sphere.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-3), f"Expected {expected_fitness}, got {fitness_value}"

if __name__ == "__main__":
    pytest.main()
