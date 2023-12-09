import re
from pathlib import Path
from typing import List

WordNum = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

WordFilter = re.compile(
    "(?=(?P<num>one|1|two|2|three|3|four|4|five|5|six|6|seven|7|eight|8|nine|9|zero|0))"
)


def get_input(input_file: Path) -> List[str]:
    with input_file.open("r", encoding="utf-8") as input:
        input = input.readlines()
    return input


def main():
    numbers = []
    input = get_input(Path("./input.txt"))
    input = [line.strip() for line in input]
    # print(input)
    for line in input:
        number = WordFilter.findall(line)
        number = [WordNum[num] if not num.isdigit() else num for num in number]
        numbers.append(number)
        print(number)
    answer = 0
    for number in numbers:
        to_add = (
            int(number[0] + number[-1])
            if len(number) > 1
            else ((int(number[0]) * 10) + int(number[0]))
        )
        print(f"number:{''.join(number)}, to_add: {to_add}")
        answer += to_add
        print(f"hellp:{answer}")
    print(f"answer: {answer}")


if __name__ == "__main__":
    main()
