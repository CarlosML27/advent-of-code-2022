from aoc22.inputs import get_relative_path, read_lines
from aoc22.solutions.day_03.puzzle_commons import get_result


def _get_rucksacks(lines: list[str]) -> list[list[str]]:
    rucksacks = [lines[x : x + 3] for x in range(0, len(lines), 3)]
    return rucksacks


def run():
    input_path = get_relative_path(__file__, 'input.txt')
    lines = read_lines(input_path)
    rucksacks = _get_rucksacks(lines)
    result = get_result(rucksacks)
    print(result)
