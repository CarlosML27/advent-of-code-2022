def get_elves_values(lines: list[str]) -> list[int]:
    size = len(lines)
    index_list = [index + 1 for index, value in enumerate(lines) if value == '']
    elves_lists = [
        lines[start : end - 1]
        for start, end in zip(
            [0] + index_list,
            index_list + ([size + 1] if index_list[-1] != size else []),
        )
        if start < end
    ]
    elves = [sum(map(int, elf_list)) for elf_list in elves_lists]
    return elves
