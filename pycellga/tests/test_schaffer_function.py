import pytest
from problems.single_objective.continuous.schaffer import Schaffer

@pytest.fixture
def setup_schaffer():
    """
    Fixture to provide an instance of the Schaffer problem with the default number of design variables.
    """
    return Schaffer(design_variables=2)

def test_schaffer_function(setup_schaffer):
    """
    Test the Schaffer function implementation.

    This test checks the calculation of the Schaffer function value for given lists of float variables.
    It uses predefined inputs and compares the outputs to the expected values.

    Parameters
    ----------
    setup_schaffer : fixture
        The fixture providing the Schaffer problem instance.
    """
    # Define sample input variables and their expected Schaffer function values
    test_cases = [
        ([0.0, 0.0], 0.75),       # Test with zeros
        ([1.0, 1.0], 0.606),      # Symmetric point
        ([2.0, -1.0], 0.674),     # Positive and negative values
        ([3.0, 4.0], 0.722)       # Larger positive values
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_schaffer.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-3), f"Expected {expected_fitness}, got {fitness_value}"

if __name__ == "__main__":
    pytest.main()
