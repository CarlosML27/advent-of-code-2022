from aoc22.inputs import get_relative_path, read_lines
from aoc22.solutions.day_03.puzzle_commons import get_common_item, get_rucksacks


def _get_rucksack_result(rucksack: tuple[str, str]) -> int:
    common_item = get_common_item(rucksack)
    ascii_lowercase_a_value = 97
    ascii_uppercase_a_value = 65
    if common_item.islower():
        result = ord(common_item) - ascii_lowercase_a_value + 1
    else:
        result = ord(common_item) - ascii_uppercase_a_value + 27
    return result


def _get_result(rucksacks: list[tuple[str, str]]) -> int:
    result = 0
    for rucksack in rucksacks:
        result = result + _get_rucksack_result(rucksack)
    return result


def run():
    input_path = get_relative_path(__file__, 'input.txt')
    lines = read_lines(input_path)
    rucksacks = get_rucksacks(lines)
    result = _get_result(rucksacks)
    print(result)
