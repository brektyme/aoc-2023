import re
from enum import Enum
from pathlib import Path
from typing import Dict, Tuple, Union, Generator

from libs import get_input


class CubesMaxes(Enum):
    RED = 12
    GREEN = 13
    BLUE = 14


game_filter = re.compile(r"^Game ([\d]+): (.*)")
cube_filter = re.compile(r"((\d+) (\w+)){1,3}")


def parse_game(
    game: str,
) -> Generator[Union[Tuple[int, Dict[str, int]], Tuple[int, None]], None, None]:
    rounds_cube = []
    matches = game_filter.findall(game)
    game_number = int(matches[0][0])
    rounds = matches[0][1].split(";")
    for round in rounds:
        cubes = round.split(",")
        cube_dict = {
            color: int(value) for _, value, color in cube_filter.findall(str(cubes))
        }
        for color, value in cube_dict.items():
            if value > CubesMaxes[color.upper()].value:
                yield game_number, None
        yield game_number, cube_dict


def main() -> None:
    games = dict()
    input = get_input(input_file=Path("input.txt"))
    for game in input:
        pg = parse_game(game)
        for game_number, game_round in pg:
            if not game_round:
                print(f"{game_number}: {games.get(game_number, None)}: {game}")
                if games.get(game_number, None):
                    del games[game_number]
                pg.close()
                break
            if not games.get(game_number, None):
                games[game_number] = []
            games[game_number].append(game_round)
    print(f"answer: {sum(games.keys())}")


if __name__ == "__main__":
    main()
