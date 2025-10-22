def part_one(input: str) -> str:
    passphrases = [x.strip() for x in input.strip().splitlines()]
    num_valid = 0
    for passphrase in passphrases:
        words = passphrase.split()
        while len(words) > 0:
            word = words.pop(0)
            if word in words:
                break
        else:
            num_valid += 1

    return str(num_valid)


def part_two(input: str) -> str:
    passphrases = [x.strip() for x in input.strip().splitlines()]
    num_valid = 0
    for passphrase in passphrases:
        words = passphrase.split()
        words_dicts: list[dict[str, int]] = []
        for word in words:
            d: dict[str, int] = dict()
            for c in word:
                d[c] = d.get(c, 0) + 1
            words_dicts.append(d)
        while len(words_dicts) > 0:
            words_dict = words_dicts.pop(0)
            if any([wd == words_dict for wd in words_dicts]):
                break
        else:
            num_valid += 1

    return str(num_valid)
