from aoc22.inputs import get_relative_path, read_lines
from aoc22.solutions.day_01.puzzle_commons import get_elves_values


def _get_result(elves: list[int]) -> int:
    return max(elves)


def run():
    input_path = get_relative_path(__file__, 'input.txt')
    lines = read_lines(input_path)
    elves = get_elves_values(lines)
    result = _get_result(elves)
    print(result)
