import os
import pathlib


def _get_base_input_path(file_path: pathlib.Path):
    base_path = pathlib.Path(file_path).resolve().parent
    return base_path


def get_relative_path(file_path: pathlib.Path, relative_path: str) -> str:
    input_path = os.path.join(_get_base_input_path(file_path), relative_path)
    return input_path


def read_lines(path: str, strip=True) -> list[str]:
    lines = []
    with open(path) as file:
        for line in file:
            if strip:
                line = line.strip()
            lines.append(line)
    return lines
