def calc(a: int, b: int, op: str) -> int:
    match op:
        case "*":
            return a * b
        case "+":
            return a + b
        # case "-":
        #    return a - b
        # case "/":
        #    return a / b
        case _:
            raise Exception("oops unhandled")


def part_one(input: str) -> str:
    result = 0
    lines = input.strip().splitlines()
    ops = lines.pop().split()
    problems = [[int(x) for x in line.split()] for line in lines]
    for x in range(len(problems[0])):
        for y in range(len(problems)):
            y2 = y + 1
            if y2 >= len(problems):
                break
            problems[y2][x] = calc(problems[y][x], problems[y2][x], ops[x])
        result += problems[-1][x]
    return str(result)


# def part_two(input: str) -> str:
#    """
#    Now digits are read right-to-left, top-to-bottom
#    64
#    23
#    314
#    +
#    ---> 4 + 431 + 623
#
#    Seems like a simple transposition, with zeroes for padding
#    640
#    230
#    314
#
#    623
#    431
#    004
#
#    The part 2 solution will do the transposition and then reuse part 1
#    """
#    result = 0
#    return str(result)
