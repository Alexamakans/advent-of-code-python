def part_one(input: str) -> str:
    def is_valid_id(id: int) -> bool:
        s = str(id)
        a = s[: len(s) // 2]
        b = s[len(s) // 2 :]
        return a != b

    invalid_id_sum = 0
    for interval in input.strip().split(","):
        low, high = [int(x) for x in interval.split("-")]
        for n in range(low, high + 1):
            if not is_valid_id(n):
                invalid_id_sum += n

    return str(invalid_id_sum)


def part_two(input: str) -> str:
    def is_valid_id(id: int) -> bool:
        s = str(id)
        if len(s) == 1:
            return True

        for length in range(1, len(s)):
            if len(s) % length != 0:
                continue
            num_parts = len(s) // length
            part = s[:length]
            for i in range(1, num_parts):
                check = s[i * length : (i + 1) * length]
                if part != check:
                    break
            else:
                # string is made of some N copies of a substring, where N is a positive integer > 1
                # examples: 121212, 11, 1, 13371337, etc.
                return False
        return True

    invalid_id_sum = 0
    for interval in input.strip().split(","):
        low, high = [int(x) for x in interval.split("-")]
        for n in range(low, high + 1):
            if not is_valid_id(n):
                invalid_id_sum += n

    return str(invalid_id_sum)
