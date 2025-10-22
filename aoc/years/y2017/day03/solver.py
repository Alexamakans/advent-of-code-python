from collections.abc import Generator
import itertools


def get_ring(spiral_index: int) -> tuple[int, int]:
    ring = 0
    max_spiral_index = 0
    while True:
        if spiral_index <= max_spiral_index:
            return ring, max_spiral_index
        ring += 1
        max_spiral_index += 8 * ring


def part_one(input: str) -> str:
    spiral_index = int(input.strip()) - 1
    ring, max_spiral_index = get_ring(spiral_index)
    max_steps = ring * 2
    min_steps = ring
    dir = -1
    cur_steps = max_steps
    cur_index = max_spiral_index
    while True:
        if cur_index == spiral_index:
            return str(cur_steps)
        cur_index -= 1
        cur_steps += dir
        if cur_steps == min_steps:
            dir = 1
        elif cur_steps == max_steps:
            dir = -1


def sum_spiral() -> Generator[int]:
    #       -y
    #    v < < < <
    #    v v < < ^
    # -x v v > ^ ^  +x
    #    v > > > ^
    #    > > > > >
    #       +y
    #
    # First part:
    #   ( 0,  0) -> ( 1,  0)  x+1 Right
    #   ( 1,  0) -> ( 1, -1)  y-1 Up
    #   ( 1, -1) -> ( 0, -1)  x-1 Left
    #   ( 0, -1) -> (-1, -1)  x-1 Left
    #   (-1, -1) -> (-1,  0)  y+1 Down
    #   (-1,  0) -> (-1,  1)  y+1 Down
    #
    # We are now at the dot (.)
    #       -y
    #    v < < < <
    #    v v < < ^
    # -x v v > ^ ^  +x
    #    v . > > ^
    #    > > > > >
    #       +y
    #
    # Let's keep going.
    #
    # RRR, UUU, LLLL, DDDD
    #
    #       -y
    #    v < < < <
    #    v v < < ^
    # -x v v > ^ ^  +x
    #    v > > > ^
    #    . > > > >
    #       +y
    #
    # The movements for the first part, next to the second part.
    #   R,   U,   LL,   DD
    # RRR, UUU, LLLL, DDDD
    #
    # The first iteration (i=0) and the second iteration (i=1) both follow the pattern of:
    #   1+2i * R, 1+2i * U, 2+2i * L, 2+2i * D

    # using a dict for the world helps with treating it as an infinite grid of zeros.
    world = {(0, 0): 1}
    x, y = 0, 0
    #        right     up      left     down
    right = (1, 0)
    up = (0, -1)
    left = (-1, 0)
    down = (0, 1)
    for steps in itertools.count(1, 2):  # 1, 3, 5, 7 etc.
        long_side_steps = steps + 1
        for _ in range(steps):
            x += right[0]
            y += right[1]
            world[x, y] = sum(
                world.get((x + dx, y + dy), 0)
                for dx in range(-1, 2)
                for dy in range(-1, 2)
            )
            yield world[x, y]
        for _ in range(steps):
            x += up[0]
            y += up[1]
            world[x, y] = sum(
                world.get((x + dx, y + dy), 0)
                for dx in range(-1, 2)
                for dy in range(-1, 2)
            )
            yield world[x, y]
        for _ in range(long_side_steps):
            x += left[0]
            y += left[1]
            world[x, y] = sum(
                world.get((x + dx, y + dy), 0)
                for dx in range(-1, 2)
                for dy in range(-1, 2)
            )
            yield world[x, y]
        for _ in range(long_side_steps):
            x += down[0]
            y += down[1]
            world[x, y] = sum(
                world.get((x + dx, y + dy), 0)
                for dx in range(-1, 2)
                for dy in range(-1, 2)
            )
            yield world[x, y]


def part_two(input: str) -> str:
    value = int(input.strip())
    for x in sum_spiral():
        if x > value:
            return str(x)
    return "unreachable"
