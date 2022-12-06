def get_strategy_guide(lines: list[str]) -> list[tuple[str, str]]:
    strategy_guide = []
    for line in lines:
        split_line = line.split()
        game_round = tuple((split_line[0], split_line[1]))
        strategy_guide.append(game_round)
    return strategy_guide
