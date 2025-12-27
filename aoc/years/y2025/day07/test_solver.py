import os

from aoc import util

from aoc.years.y2025.day07 import solver

dir_path = os.path.dirname(os.path.realpath(__file__))


def test_part_one_samples_are_correct():
    sample_cases = [x for x in util.load_samples(dir_path) if x.part_mask & 1 == 1]
    for sample_case in sample_cases:
        assert solver.part_one(sample_case.input) == sample_case.expected_result


def test_part_one_is_correct():
    input = util.load_input_from_path(os.path.join(dir_path, "input"))
    assert solver.part_one(input) == "1717"


def test_part_two_samples_are_correct():
    sample_cases = [x for x in util.load_samples(dir_path) if x.part_mask & 2 == 2]
    for sample_case in sample_cases:
        assert solver.part_two(sample_case.input) == sample_case.expected_result


def test_part_two_is_correct():
    input = util.load_input_from_path(os.path.join(dir_path, "input"))
    assert solver.part_two(input) == "231507396180012"
