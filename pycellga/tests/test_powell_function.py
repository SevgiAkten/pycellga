import pytest
from problems.single_objective.continuous.powell import Powell

@pytest.fixture
def setup_powell():
    """
    Fixture to provide an instance of the Powell problem.
    """
    return Powell(design_variables=8)  

def test_powell_function(setup_powell):
    """
    Test the Powell function implementation.

    Bu test, verilen değişken listeleri için Powell fonksiyonunun doğruluğunu kontrol eder.
    Belirli girişler ve beklenen çıktılarla çalışır.

    Parameters
    ----------
    setup_powell : fixture
        Powell problem örneğini sağlayan fixture.
    """
    test_cases = [
        ([0.0, 0.0, 0.0, 0.0], 0.0),  
        ([1.0, 2.0, 3.0, 4.0], 1512.0),  
        ([1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0], 3024.0),  
        ([5.0, -4.0, 0.0, 0.0, 2.0, -3.0, 4.0, -5.0], 47571.0)  
    ]

    for variables, expected_fitness in test_cases:
        setup_powell.design_variables = len(variables)  
        fitness_value = setup_powell.f(variables)
        print(f"Variables: {variables} => Fitness: {fitness_value}, Expected: {expected_fitness}")
        assert isinstance(fitness_value, float)
        assert fitness_value == pytest.approx(expected_fitness, rel=1e-1), f"Expected {expected_fitness}, got {fitness_value}"
