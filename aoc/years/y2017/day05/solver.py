# numba and numpy for make go fast, zoooom
from numba import (  # pyright: ignore[reportMissingTypeStubs]
    njit,  # pyright: ignore[reportUnknownVariableType]
)
from numpy import ndarray
import numpy as np


def part_one(input: str) -> str:
    offsets = [int(x) for x in input.strip().splitlines()]
    cur_index = 0
    num_jumps = 0
    while True:
        offset = offsets[cur_index]
        offsets[cur_index] += 1
        cur_index += offset
        num_jumps += 1
        if cur_index < 0 or cur_index >= len(offsets):
            break
    return str(num_jumps)


def part_two(input: str) -> str:
    offsets = [int(x) for x in input.splitlines()]

    return str(_part_two(np.array(offsets, dtype=np.int64)))


@njit
def _part_two(offsets: ndarray):
    cur_index = 0
    num_jumps = 0
    num_offsets = len(offsets)
    while 0 <= cur_index < num_offsets:
        offset = offsets[cur_index]  # pyright: ignore[reportAny]
        offsets[cur_index] = offset - 1 if offset >= 3 else offset + 1
        cur_index += offset  # pyright: ignore[reportAny]
        num_jumps += 1
    return num_jumps
