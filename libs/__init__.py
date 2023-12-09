from pathlib import Path
from typing import List


def get_input(input_file: Path) -> List[str]:
    with input_file.open("r", encoding="utf-8") as input:
        input = input.readlines()
    return input
