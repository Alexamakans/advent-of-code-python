import os
import csv
from typing import final

dir_path = os.path.dirname(os.path.realpath(__file__))


@final
class SampleCase:
    def __init__(self, part_mask: int, input: str, expected_result: str):
        self.part_mask = part_mask
        self.input = input
        self.expected_result = expected_result


def load_samples(base_path: str) -> list[SampleCase]:
    cases: list[SampleCase] = []
    with open(f"{base_path}/samples.csv") as f:
        r = csv.reader(f, delimiter=",", quotechar='"')
        for row in r:
            sample_case = SampleCase(int(row[0]), row[1], row[2])
            cases.append(sample_case)
    return cases


def load_input(year: int, day: int) -> str:
    p = os.path.join(dir_path, "years", f"y{year}", f"day{day:02}", "input")
    return load_input_from_path(p)


def load_input_from_path(p: str) -> str:
    with open(p) as f:
        return f.read()
