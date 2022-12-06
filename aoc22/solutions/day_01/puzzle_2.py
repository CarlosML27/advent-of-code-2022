from aoc22.inputs import get_relative_path, read_lines
from aoc22.solutions.day_01.puzzle_commons import get_elves_values


def _sum_max_numbers(check_list: list[int], top_n: int) -> int:
    return sum(sorted(check_list)[-top_n:])


def _get_result(elves: list[int]) -> int:
    return _sum_max_numbers(elves, 3)


def run():
    input_path = get_relative_path(__file__, 'input.txt')
    lines = read_lines(input_path)
    elves = get_elves_values(lines)
    result = _get_result(elves)
    print(result)
