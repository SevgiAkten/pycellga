import pytest
from problems.single_objective.continuous.chichinadze import Chichinadze

@pytest.fixture
def setup_chichinadze():
    """
    Fixture for creating an instance of the Chichinadze problem.

    Returns
    -------
    Chichinadze
        An instance of the Chichinadze problem.
    """
    return Chichinadze()

def test_chichinadze_function(setup_chichinadze):
    """
    Test the Chichinadze function implementation.

    This test checks the calculation of the Chichinadze function value for given lists of float variables.
    It uses predefined inputs and compares the outputs to the expected values.

    Parameters
    ----------
    setup_chichinadze : fixture
        The fixture providing the Chichinadze problem instance.
    """
    # Define sample input variables and their expected Chichinadze function values
    test_cases = [
        ([5.90133, 0.5], -43.3159),  # Global minimum
        ([0.0, 0.0], 20.6066),  # Point at the origin
        ([-30.0, 30.0], 1261.0),  # Point at the boundary
        ([10.0, -10.0], -19.0),  # Arbitrary point
        ([15.0, 15.0], 56.0)  # Another arbitrary point
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_chichinadze.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-4), f"Expected {expected_fitness}, got {fitness_value}"

if __name__ == "__main__":
    pytest.main()
