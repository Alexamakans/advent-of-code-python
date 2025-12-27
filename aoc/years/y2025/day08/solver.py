import math
from typing import NamedTuple


class JunctionBox(NamedTuple):
    x: int
    y: int
    z: int


def part_one(input: str, pair_count: int = 1000) -> str:
    boxes = [
        JunctionBox(*(int(x) for x in line.split(","))) for line in input.splitlines()
    ]
    pairs_by_distance: list[list[JunctionBox]] = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            pairs_by_distance.append([boxes[i], boxes[j]])
    pairs_by_distance.sort(
        key=lambda pair: (pair[0].x - pair[1].x) ** 2
        + (pair[0].y - pair[1].y) ** 2
        + (pair[0].z - pair[1].z) ** 2
    )

    circuits: list[set[JunctionBox]] = []
    for i in range(pair_count):
        pair = pairs_by_distance[i]
        for circuit in circuits:
            if pair[0] in circuit and pair[1] in circuit:
                break
        else:
            pair_a_index = -1
            pair_b_index = -1
            for i, circuit in enumerate(circuits):
                if pair[0] in circuit:
                    pair_a_index = i
                if pair[1] in circuit:
                    pair_b_index = i
            if pair_a_index != -1 and pair_b_index != -1:
                # the index is guaranteed to be different due to the for-if-break
                a = circuits[pair_a_index]
                b = circuits[pair_b_index]
                circuits[pair_a_index] = a.union(b)
                circuits.remove(b)
            elif pair_a_index != -1:
                a = circuits[pair_a_index]
                a.add(pair[1])
            elif pair_b_index != -1:
                b = circuits[pair_b_index]
                b.add(pair[0])
            else:
                circuit: set[JunctionBox] = set()
                circuit.add(pair[0])
                circuit.add(pair[1])
                circuits.append(circuit)

    circuits.sort(key=lambda circuit: len(circuit), reverse=True)
    result = math.prod((len(circuit) for circuit in circuits[:3]))
    return str(result)


def part_two(input: str) -> str:
    boxes = [
        JunctionBox(*(int(x) for x in line.split(","))) for line in input.splitlines()
    ]
    pairs_by_distance: list[list[JunctionBox]] = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            pairs_by_distance.append([boxes[i], boxes[j]])
    pairs_by_distance.sort(
        key=lambda pair: (pair[0].x - pair[1].x) ** 2
        + (pair[0].y - pair[1].y) ** 2
        + (pair[0].z - pair[1].z) ** 2
    )

    circuits: list[set[JunctionBox]] = []
    i = 0
    last_pair: list[JunctionBox] = []
    while not (len(circuits) == 1 and len(circuits[0]) == len(boxes)):
        pair = pairs_by_distance[i]
        last_pair = pair
        i += 1
        for circuit in circuits:
            if pair[0] in circuit and pair[1] in circuit:
                break
        else:
            pair_a_index = -1
            pair_b_index = -1
            for circuit_index, circuit in enumerate(circuits):
                if pair[0] in circuit:
                    pair_a_index = circuit_index
                if pair[1] in circuit:
                    pair_b_index = circuit_index
            if pair_a_index != -1 and pair_b_index != -1:
                # the index is guaranteed to be different due to the for-if-break
                a = circuits[pair_a_index]
                b = circuits[pair_b_index]
                circuits[pair_a_index] = a.union(b)
                circuits.remove(b)
            elif pair_a_index != -1:
                a = circuits[pair_a_index]
                a.add(pair[1])
            elif pair_b_index != -1:
                b = circuits[pair_b_index]
                b.add(pair[0])
            else:
                circuit: set[JunctionBox] = set()
                circuit.add(pair[0])
                circuit.add(pair[1])
                circuits.append(circuit)

    return str(last_pair[0].x * last_pair[1].x)
