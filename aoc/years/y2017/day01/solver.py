def part_one(input: str) -> str:
    arr = input.strip()
    arr += arr[0]
    return str(
        sum([int(x) for i, x in enumerate(arr) if i < len(arr) - 1 and x == arr[i + 1]])
    )


def part_two(input: str) -> str:
    arr = input.strip()
    half = len(arr) // 2
    return str(
        sum([int(x) for i, x in enumerate(arr) if x == arr[(i + half) % len(arr)]])
    )
