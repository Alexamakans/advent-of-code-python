def part_one(input: str) -> str:
    dial = 50
    result = 0
    for line in input.strip().splitlines():
        sign = 1 if line[0] == "R" else -1
        value = int(line[1:])
        dial += sign * value
        while dial < 0:
            dial += 100
        while dial > 99:
            dial -= 100
        if dial == 0:
            result += 1

    return str(result)


def part_two(input: str) -> str:
    dial = 50
    result = 0
    for line in input.strip().splitlines():
        sign = 1 if line[0] == "R" else -1
        value = int(line[1:])
        full = value // 100
        partial = value % 100
        print(
            f"Dial: {dial}, Sign: {sign}, Value: {value}, Full: {full}, Partial: {partial}"
        )
        no_partial = False
        if dial == 0:
            no_partial = True
        dial += sign * partial
        result += full

        if dial < 0:
            dial += 100
            if not no_partial:
                result += 1
        elif dial > 99:
            dial -= 100
            if not no_partial:
                result += 1
        elif dial == 0 and partial != 0:
            result += 1
        print(f"-> Dial: {dial}, Result: {result}")

    return str(result)
