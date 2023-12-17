from dataclasses import dataclass
from functools import reduce
from pathlib import Path
from typing import List

from libs import get_input


@dataclass
class Position:
    row: int
    column: int


@dataclass
class EngineSymbol:
    position: Position
    symbol: str


@dataclass
class EnginePartNumber:
    number: int
    positions: List[Position]


def find_adjacent(engine_part: EnginePartNumber, symbols: List[EngineSymbol]) -> bool:
    row = engine_part.positions[0].row
    for symbol in symbols:
        if symbol.position.column in list(
            range(
                (
                    engine_part.positions[0].column - 1
                    if engine_part.positions[0].column > 0
                    else 0
                ),
                (engine_part.positions[-1].column + 2),
            )
        ) and (
            symbol.position.row in list(range(row - 1 if row > 0 else 0, row + 2))
            or symbol.position.row == row
        ):
            return True
    return False


def main():
    engine_schema = get_input(Path("input.txt"))
    symbols: List[EngineSymbol] = []
    adjacents: List[int] = []
    part_numbers: List[EnginePartNumber] = []
    part_number = ""
    part_number_positions: List[Position] = []
    for row, line in enumerate(engine_schema):
        for col, char in enumerate(line.strip()):
            try:
                int(char)
                part_number += char
                part_number_positions.append(Position(row=row, column=col))
                continue
            except ValueError as _:
                if part_number:
                    engine_part = EnginePartNumber(
                        number=int(part_number), positions=part_number_positions
                    )
                    part_numbers.append(engine_part)
                    part_number = ""
                    part_number_positions = []
            _ = (
                symbols.append(
                    EngineSymbol(symbol=char, position=Position(row=row, column=col))
                )
                if not char == "."
                else None
            )
    for e_part in part_numbers:
        adjacent = find_adjacent(e_part, symbols)
        if adjacent:
            adjacents.append(e_part.number)
    print(adjacents)
    print(f"answer: {reduce(lambda x, y: x + y, adjacents)}")


if __name__ == "__main__":
    main()
