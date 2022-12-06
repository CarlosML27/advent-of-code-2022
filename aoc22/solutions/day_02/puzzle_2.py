from aoc22.inputs import get_relative_path, read_lines
from aoc22.solutions.day_02.puzzle_commons import get_outcome_result, get_strategy_guide


def _get_player_result(rival_score: int, instruction: int) -> int:
    player_score = rival_score
    if instruction == 1:
        rival_score = rival_score + 3 if rival_score == 1 else rival_score
        player_score = rival_score - 1
    elif instruction == 3:
        rival_score = 0 if rival_score == 3 else rival_score
        player_score = rival_score + 1
    return player_score


def _get_round_result(game_round: tuple[str, str]) -> int:
    ascii_uppercase_a_value = 65
    ascii_uppercase_x_value = 88
    rival_score = ord(game_round[0]) - ascii_uppercase_a_value + 1
    instruction = ord(game_round[1]) - ascii_uppercase_x_value + 1
    player_score = _get_player_result(rival_score, instruction)
    outcome = get_outcome_result(player_score, rival_score)
    return player_score + outcome


def _get_result(guide: list[tuple[str, str]]) -> int:
    result = 0
    for game_round in guide:
        result = result + _get_round_result(game_round)
    return result


def run():
    input_path = get_relative_path(__file__, 'input.txt')
    lines = read_lines(input_path)
    strategy_guide = get_strategy_guide(lines)
    result = _get_result(strategy_guide)
    print(result)
