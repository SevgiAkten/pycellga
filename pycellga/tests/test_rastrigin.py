import pytest
from problems.single_objective.continuous.rastrigin import Rastrigin

@pytest.fixture
def setup_rastrigin():
    """
    Fixture to provide an instance of the Rastrigin problem.
    """
    return Rastrigin(design_variables=4)

def test_rastrigin(setup_rastrigin):
    """
    Test the Rastrigin function implementation.

    This test verifies the calculation of the Rastrigin function value for a given list of continuous variables.
    It compares the function output with known expected values.

    Parameters
    ----------
    setup_rastrigin : fixture
        The fixture providing the Rastrigin problem instance.
    """
    # Test cases with known values
    test_cases = [
        ([2.305, -4.025, 3.805, -1.505], 78.375),
        ([-4.995, -2.230, -3.706, 2.305], 83.839),
        ([0.0, 0.0, 0.0, 0.0], 0.0)  # Global minimum
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_rastrigin.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-3), f"Expected {expected_fitness}, got {fitness_value}"

if __name__ == "__main__":
    pytest.main()
