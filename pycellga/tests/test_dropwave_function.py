import pytest
from problems.single_objective.continuous.dropwave import Dropwave

@pytest.fixture
def setup_dropwave():
    """
    Fixture for creating an instance of the Dropwave problem.

    Returns
    -------
    Dropwave
        An instance of the Dropwave problem.
    """
    return Dropwave()

def test_dropwave_function(setup_dropwave):
    """
    Test the Dropwave function implementation.

    This test checks the calculation of the Dropwave function value for given lists of float variables.
    It uses predefined inputs and compares the outputs to the expected values.

    Parameters
    ----------
    setup_dropwave : fixture
        The fixture providing the Dropwave problem instance.
    """
    # Define sample input variables and their expected Dropwave function values
    test_cases = [
        ([0.0, 0.0], -1.0),  # Global minimum
        ([5.12, 5.12], -0.052),  # Boundary point
        ([-5.12, -5.12], -0.052),  # Boundary point
        ([2.5, -2.5], -0.123),  # Arbitrary point
        ([-3.0, 1.0], -0.281)  # Another arbitrary point
    ]

    for variables, expected_fitness in test_cases:
        # Ensure the input length matches the number of variables
        assert len(variables) == setup_dropwave.num_variables, \
            f"Input length does not match the expected number of variables ({setup_dropwave.num_variables})."

        fitness_value = setup_dropwave.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-3), f"Expected {expected_fitness}, got {fitness_value}"

if __name__ == "__main__":
    pytest.main()
