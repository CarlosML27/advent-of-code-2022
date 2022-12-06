from aoc22.inputs import get_relative_path, read_lines
from aoc22.solutions.day_03.puzzle_commons import get_result


def _get_rucksacks(lines: list[str]) -> list[list[str]]:
    rucksacks = []
    for line in lines:
        first_compartment = line[: len(line) // 2]
        second_compartment = line[len(line) // 2 :]
        rucksack = [first_compartment, second_compartment]
        rucksacks.append(rucksack)
    return rucksacks


def run():
    input_path = get_relative_path(__file__, 'input.txt')
    lines = read_lines(input_path)
    rucksacks = _get_rucksacks(lines)
    result = get_result(rucksacks)
    print(result)
