def get_rucksacks(lines: list[str]) -> list[tuple[str, str]]:
    rucksacks = []
    for line in lines:
        first_compartment = line[: len(line) // 2]
        second_compartment = line[len(line) // 2 :]
        rucksack = tuple((first_compartment, second_compartment))
        rucksacks.append(rucksack)
    return rucksacks


def get_common_item(rucksack: tuple[str, str]) -> str:
    return ''.join(set(rucksack[0]).intersection(rucksack[1]))
