from enum import Enum
from typing import NamedTuple


class Tile(Enum):
    EMPTY = "."
    START = "S"
    SPLITTER = "^"


class Position(NamedTuple):
    x: int
    y: int


# [y][x]
type M = list[list[Tile]]


def parse(input: str) -> tuple[M, Position]:
    m: M = []
    start_pos = Position(-1, -1)
    for y, line in enumerate(input.strip().splitlines()):
        row: list[Tile] = []
        for x, c in enumerate(line):
            tile = Tile(c)
            row.append(tile)
            if tile == Tile.START:
                start_pos = Position(x, y)
        m.append(row)
    return m, start_pos


def part_one(input: str) -> str:
    result = 0
    m, start_pos = parse(input)
    beams = [start_pos]
    visited: set[Position] = set()
    while len(beams) > 0:
        beam = beams.pop()
        if beam in visited:
            continue
        visited.add(beam)

        next_y = beam.y + 1
        if next_y >= len(m):
            continue

        if m[next_y][beam.x] == Tile.SPLITTER:
            result += 1
            x1 = beam.x - 1
            if x1 >= 0:
                beams.append(Position(x1, next_y))
            x2 = beam.x + 1
            if x2 < len(m[next_y]):
                beams.append(Position(x2, next_y))
        else:
            beams.append(Position(beam.x, next_y))
    return str(result)


def part_two(input: str) -> str:
    m, start_pos = parse(input)
    m_visited_count = [[0 for _ in range(len(m[0]))] for _ in range(len(m))]
    m_visited_count[start_pos.y][start_pos.x] = 1
    beams = [start_pos]
    visited: set[Position] = set()
    while len(beams) > 0:
        beam = beams.pop(0)
        if beam in visited:
            continue
        visited.add(beam)

        next_y = beam.y + 1
        if next_y >= len(m):
            continue

        if m[next_y][beam.x] == Tile.SPLITTER:
            x1 = beam.x - 1
            if x1 >= 0:
                beams.append(Position(x1, next_y))
                m_visited_count[next_y][x1] += m_visited_count[beam.y][beam.x]
            x2 = beam.x + 1
            if x2 < len(m[next_y]):
                beams.append(Position(x2, next_y))
                m_visited_count[next_y][x2] += m_visited_count[beam.y][beam.x]
        else:
            beams.append(Position(beam.x, next_y))
            m_visited_count[next_y][beam.x] += m_visited_count[beam.y][beam.x]
    return str(sum(x for x in m_visited_count[-1]))
