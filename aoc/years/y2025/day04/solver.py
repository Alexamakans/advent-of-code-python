# returns the modified m and the number of rolls removed
def remove_rolls(m: list[str]) -> tuple[list[str], int]:
    result = 0

    # [y][x]
    h = len(m)
    w = len(m[0])
    conv: list[list[int]] = [[0 for _ in range(w)] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            cur = m[y][x]
            if cur == ".":
                conv[y][x] = 100000
            else:
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        check_x = x + dx
                        check_y = y + dy
                        if check_x < 0 or check_x >= w:
                            continue
                        if check_y < 0 or check_y >= w:
                            continue
                        check = m[check_y][check_x]
                        if check == "@":
                            conv[y][x] += 1
    for y in range(h):
        for x in range(w):
            if conv[y][x] < 4 and m[y][x] == "@":
                result += 1
                m[y] = m[y][:x] + "." + m[y][x + 1 :]

    return m, result


def part_one(input: str) -> str:
    # [y][x]
    m = input.strip().splitlines()
    _, result = remove_rolls(m)
    return str(result)


def part_two(input: str) -> str:
    result = 0
    # [y][x]
    m = input.strip().splitlines()
    while True:
        m, r = remove_rolls(m)
        if r == 0:
            break
        result += r

    return str(result)
