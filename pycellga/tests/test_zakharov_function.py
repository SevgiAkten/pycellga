import pytest
from problems.single_objective.continuous.zakharov import Zakharov

@pytest.fixture
def setup_zakharov():
    """
    Fixture to provide an instance of the Zakharov problem.
    """
    return Zakharov(design_variables=2)

def test_zakharov_function(setup_zakharov):
    """
    Test the Zakharov function implementation.

    This test checks the calculation of the Zakharov function value
    for given lists of float variables. It uses predefined inputs and compares
    the outputs to the expected values.
    """
    # Define sample input variables and their expected Zakharov function values
    test_cases = [
        ([0.0, 0.0], 0.0),                # Global minimum
        ([1.0, 1.0], 9.312),              # Arbitrary point
        ([2.0, -1.0], 5.0),               # Another arbitrary point
    ]

    # Testing 3 variables requires initializing with design_variables=3
    three_var_problem = Zakharov(design_variables=3)
    extended_test_case = ([1.0, 2.0, 3.0], 2464.0)

    # Run test cases with default 2-variable problem
    for variables, expected_fitness in test_cases:
        fitness_value = setup_zakharov.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-3), f"Expected {expected_fitness}, got {fitness_value}"

    # Run test case with 3-variable problem
    variables, expected_fitness = extended_test_case
    fitness_value = three_var_problem.f(variables)
    print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
    assert isinstance(fitness_value, float)
    assert fitness_value == pytest.approx(expected_fitness, rel=1e-3), f"Expected {expected_fitness}, got {fitness_value}"

if __name__ == "__main__":
    pytest.main()
