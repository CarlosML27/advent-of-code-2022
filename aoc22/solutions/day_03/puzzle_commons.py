def get_common_item(rucksack: list[str]) -> str:
    rucksack = list(map(set, rucksack))
    return ''.join(set.intersection(*rucksack))


def get_rucksack_result(rucksack: list[str]) -> int:
    common_item = get_common_item(rucksack)
    ascii_lowercase_a_value = 97
    ascii_uppercase_a_value = 65
    if common_item.islower():
        result = ord(common_item) - ascii_lowercase_a_value + 1
    else:
        result = ord(common_item) - ascii_uppercase_a_value + 27
    return result
