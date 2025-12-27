# please don't look


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


def solve_problems(ops: list[str], problems: list[list[int]]) -> int:
    result = 0
    for x in range(len(problems[0])):
        for y in range(len(problems)):
            y2 = y + 1
            if y2 >= len(problems):
                break
            if problems[y2][x] == 0:
                # hack to prevent having to do proper thing somewhere else
                problems[y2][x] = problems[y][x]
                print("skip")
            else:
                print(f"{problems[y][x]} {ops[x]} {problems[y2][x]}")
                problems[y2][x] = calc(problems[y][x], problems[y2][x], ops[x])
        print("=", problems[-1][x])
        result += problems[-1][x]
    return result


def part_one(input: str) -> str:
    lines = input.strip().splitlines()
    ops = lines.pop().split()
    problems = [[int(x) for x in line.split()] for line in lines]
    return str(solve_problems(ops, problems))


def part_two(input: str) -> str:
    # Compared to part 1, we first chunk the non-operator lines based on the index of the operators.
    # This is because we want to maintain the matrix structure for our transposition.

    # important to not strip due to how we chunk the problems
    lines = input.splitlines()

    ops_line = lines.pop()
    ops = ops_line.split()
    ops_indices: list[int] = [0]
    cp_ops = list(ops[1:])
    while len(cp_ops) > 0:
        op = cp_ops[0]
        cp_ops = cp_ops[1:]
        start = ops_indices[-1] + 1
        i = ops_line.index(op, start)
        ops_indices.append(i)
    ops_indices.append(len(ops_line) + 1)

    # [y][x]
    problems_pretranspose: list[list[list[str]]] = [
        [["a"]] * len(ops) for _ in range(len(lines))
    ]
    for i in range(len(ops_indices) - 1):
        j = i + 1
        for y, line in enumerate(lines):
            start = ops_indices[i]
            end = ops_indices[j]
            value = line[start : end - 1]
            problems_pretranspose[y][i] = list(value)

    problems = [[0 for _ in range(len(ops))] for _ in range(len(lines))]
    for x in range(len(ops)):
        problem: list[list[str]] = []
        for y in range(len(lines)):
            problem.append(problems_pretranspose[y][x])
        transposed = ["".join(x) for x in zip(*problem)]
        # print(lines)
        for y in range(len(transposed)):
            problems[y][x] = int(transposed[y])

    return str(solve_problems(ops, problems))
