from dataclasses import dataclass
from functools import reduce
from pathlib import Path
from typing import List, Dict, Any

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


def find_adjacent(
    symbol: EngineSymbol, engine_parts: List[EnginePartNumber]
) -> tuple[bool, list[EnginePartNumber]]:
    row = symbol.position.row
    adjacent_parts = []
    adjacent = False
    for e_part in engine_parts:
        e_row = e_part.positions[0].row
        if symbol.symbol != "*":
            continue
        if symbol.position.column in list(
            range(
                (
                    e_part.positions[0].column - 1
                    if e_part.positions[0].column > 0
                    else 0
                ),
                (e_part.positions[-1].column + 2),
            )
        ) and (
            symbol.position.row in list(range(e_row - 1 if e_row > 0 else 0, e_row + 2))
        ):
            adjacent = True
            adjacent_parts.append(e_part)
    return adjacent, adjacent_parts


def main():
    engine_schema = get_input(Path("input.txt"))
    symbols: List[EngineSymbol] = []
    adjacents: List[Dict[Any, Any]] = []
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
                if char == "*"
                else None
            )
    if part_number:
        engine_part = EnginePartNumber(
            number=int(part_number), positions=part_number_positions
        )
        part_numbers.append(engine_part)
        part_number = ""
        part_number_positions = []
    for symbol in symbols:
        adjacent, e_parts = find_adjacent(symbol=symbol, engine_parts=part_numbers)
        _ if len(e_parts) != 2 else adjacents.append(
            {"symbol": symbol, "engine_parts": e_parts}
        )
    gears = []
    for adjacent in adjacents:
        gear = []
        for e_part in adjacent["engine_parts"]:
            gear.append(e_part.number)
        gears.append(gear)
    answer = reduce(lambda x, y: x + y, [gear[0] * gear[1] for gear in gears])
    print(f"answer {answer}")


if __name__ == "__main__":
    main()
