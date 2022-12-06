def get_strategy_guide(lines: list[str]) -> list[tuple[str, str]]:
    strategy_guide = []
    for line in lines:
        split_line = line.split()
        game_round = tuple((split_line[0], split_line[1]))
        strategy_guide.append(game_round)
    return strategy_guide


def get_outcome_result(player_score: int, rival_score: int) -> int:
    result = 0
    if player_score == rival_score:
        result = 3
    elif (
        (player_score == 1 and rival_score == 3)
        or (player_score == 2 and rival_score == 1)
        or (player_score == 3 and rival_score == 2)
    ):
        result = 6
    return result
