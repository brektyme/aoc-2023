import re
from functools import reduce
from pathlib import Path

from libs import get_input

game_filter = re.compile(r"^Game (\d+): (.*)")
cube_filter = re.compile(r"((\d+) (\w+)){1,3}")


def parse_game(
    game: str,
) -> tuple[int, int]:
    cube_mins = {}
    matches = game_filter.findall(game)
    game_number = int(matches[0][0])
    rounds = matches[0][1].split(";")
    for round in rounds:
        cubes = round.split(",")
        cube_dict = {
            color: int(value) for _, value, color in cube_filter.findall(str(cubes))
        }
        for color, value in cube_dict.items():
            if not cube_mins.get(color, None) or value > cube_mins.get(color, None):
                cube_mins[color] = value
    cube_pow = reduce(lambda x, y: x * y, [*cube_mins.values()])
    return game_number, cube_pow


def main() -> None:
    games = dict()
    input = get_input(input_file=Path("input.txt"))
    for game in input:
        game_number, cube_pow = parse_game(game)
        games[game_number] = cube_pow
    print(f"answer: {sum(games.values())}")


if __name__ == "__main__":
    main()
