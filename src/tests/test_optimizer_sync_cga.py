import pytest
import numpy as np
from population import Population
from selection.tournament_selection import TournamentSelection
from recombination.one_point_crossover import OnePointCrossover
from mutation.bit_flip_mutation import BitFlipMutation
from problems.single_objective.continuous.ackley import Ackley

from optimizer_sync_cga import *

@pytest.fixture
def optimization_parameters():
    return {
        'n_cols': 5,
        'n_rows': 5,
        'n_gen': 50,
        'ch_size': 10,
        'gen_type': 'Binary',
        'p_crossover': 0.8,
        'p_mutation': 0.01,
        'known_best': 10.0,
        'k_tournament': 3,
        'problem': Ackley(),
        'selection': TournamentSelection,
        'recombination': OnePointCrossover,
        'mutation': BitFlipMutation
    }

def test_optimizer_cga(optimization_parameters):
    result, params, best_objectives, avg_objectives, elapsed_time = sync_cga(
        optimization_parameters['n_cols'],
        optimization_parameters['n_rows'],
        optimization_parameters['n_gen'],
        optimization_parameters['ch_size'],
        optimization_parameters['gen_type'],
        optimization_parameters['p_crossover'],
        optimization_parameters['p_mutation'],
        optimization_parameters['known_best'],
        optimization_parameters['k_tournament'],
        optimization_parameters['problem'],
        optimization_parameters['selection'],
        optimization_parameters['recombination'],
        optimization_parameters['mutation']
    )

    assert isinstance(result, dict)
    assert isinstance(params, dict)
    assert isinstance(best_objectives, list)
    assert isinstance(avg_objectives, list)
    assert isinstance(elapsed_time, float)
    assert 'best_solution_chromosome' in result
    assert 'best_solution' in result
    assert 'found_at_generation' in result
    assert 'known_best_solution' in result
    assert 'gap' in result
    assert params['number_of_generation'] == optimization_parameters['n_gen']
    assert params['population_size'] == optimization_parameters['n_cols'] * optimization_parameters['n_rows']
    assert pytest.approx(params['probability_of_crossover']) == optimization_parameters['p_crossover'] * 100
    assert pytest.approx(params['probability_of_mutation']) == optimization_parameters['p_mutation'] * 100
    assert params['tournament_selection'] == optimization_parameters['k_tournament']

