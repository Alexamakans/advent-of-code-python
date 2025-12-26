from typing import Self, override


class Range:
    def __init__(self, low: int, high: int) -> None:
        self.low: int = low
        self.high: int = high

    def __len__(self) -> int:
        return self.high - self.low + 1

    @override
    def __eq__(self, other: object):
        if not isinstance(other, Range):
            return NotImplemented
        return self.low == other.low and self.high == other.high

    @override
    def __hash__(self) -> int:
        return (self.high << 128) | (self.low)

    def contains(self, value: int) -> bool:
        return self.low <= value <= self.high

    # if the ranges are equal, return False
    # if merged, both self and other will represent the same range, and True is returned
    # if not merged, they are left untouched and False is returned.
    def merge(self, other: Self) -> bool:
        if self == other:
            return False
        merged = False
        if self.contains(other.low):
            other.low = self.low
            merged = True
        if other.contains(self.low):
            self.low = other.low
            merged = True
        if self.contains(other.high):
            other.high = self.high
            merged = True
        if other.contains(self.high):
            self.high = other.high
            merged = True
        if merged:
            print(f"merged, eq? {self == other}")
        return merged


def part_one(input: str) -> str:
    """
    Count the number of fresh ingredients.
    An ingredient is fresh if it is contained within any of the provided ranges.

    The ranges are inclusive, 1-3 means 1, 2, 3.

    Input:
    <range-1-start>-<range-1-end>
    <range-2-start>-<range-2-end>

    <ingredient-1>
    <ingredient-2>
    """
    result = 0
    ranges: list[Range] = []
    lines = input.strip().splitlines()
    i = 0
    for line in lines:
        i += 1
        if not line.strip():
            break
        low, high = [int(x) for x in line.split("-")]
        ranges.append(Range(low, high))

    for line in lines[i:]:
        ingredient = int(line)
        for r in ranges:
            if r.contains(ingredient):
                result += 1
                break

    return str(result)


def part_two(input: str) -> str:
    """
    Same thing but consider all ingredients to be available.
    The second section of the input is ignored.
    """
    result = 0
    ranges: list[Range] = []
    lines = input.strip().splitlines()
    for line in lines:
        if not line.strip():
            break
        low, high = [int(x) for x in line.split("-")]
        ranges.append(Range(low, high))

    keep_going = True
    while keep_going:
        keep_going = False
        for i in range(len(ranges)):
            cur = ranges[i]
            for j in range(i + 1, len(ranges)):
                if cur.merge(ranges[j]):
                    keep_going = True
    ranges_set = set(ranges)
    for r in ranges_set:
        result += len(r)
    return str(result)
