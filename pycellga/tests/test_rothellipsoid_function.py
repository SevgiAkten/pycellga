import pytest
from problems.single_objective.continuous.rothellipsoid import Rothellipsoid

@pytest.fixture
def setup_rothellipsoid():
    """
    Fixture to provide an instance of the Rotated Hyper-Ellipsoid problem.
    """
    return Rothellipsoid(design_variables=3)

def test_rothellipsoid_function(setup_rothellipsoid):
    """
    Test the Rotated Hyper-Ellipsoid function implementation.

    This test checks the calculation of the Rotated Hyper-Ellipsoid function value for given lists of float variables.
    It uses predefined inputs and compares the outputs to the expected values.

    Parameters
    ----------
    setup_rothellipsoid : fixture
        The fixture providing the Rotated Hyper-Ellipsoid problem instance.
    """
    # Define sample input variables and their expected Rotated Hyper-Ellipsoid function values
    test_cases = [
        ([0.0, 0.0, 0.0], 0.0),       # Global minimum
        ([1.0, 1.0, 1.0], 6.0),       
        ([2.0, 2.0, 2.0], 24.0),      
        ([1.0, 2.0, 3.0], 36.0),      
        ([5.0, -5.0, 0.0], 75.0)      
    ]

    for variables, expected_fitness in test_cases:
        fitness_value = setup_rothellipsoid.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-3), f"Expected {expected_fitness}, got {fitness_value}"

def test_rothellipsoid_evaluate(setup_rothellipsoid):
    """
    Test the Rotated Hyper-Ellipsoid function using the evaluate method.
    Ensures that evaluate produces the correct fitness value when used with pymoo.
    """
    test_case = [1.0, 1.0, 1.0]
    expected_fitness = 6.0
    result = {}
    setup_rothellipsoid.evaluate(test_case, result)
    
    fitness_value = result["F"]
    print(f"Variables: {test_case} => Fitness from evaluate: {fitness_value}, Expected: {expected_fitness}")
    assert isinstance(fitness_value, float)
    assert fitness_value == pytest.approx(expected_fitness, rel=1e-3), f"Expected {expected_fitness}, got {fitness_value}"

if __name__ == "__main__":
    pytest.main()
