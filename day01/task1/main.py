import re
from pathlib import Path
from typing import List

WordFilter = {
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


def get_input(input_file: Path) -> List[str]:
    with input_file.open("r", encoding="utf-8") as input:
        input = input.readlines()
    return input


def main():
    numbers = []
    input = get_input(Path("input.txt"))
    input = [line.strip() for line in input]
    print(input)
    for line in input:
        word = ""
        for c in line:
            if re.match("[a-zA-Z]", c):
                word += c
                if WordFilter.get(word):
                    numbers.append(WordFilter.get(word))
                    word = ""
                continue
        numbers.append("".join(re.findall("\d+", line)))
    print(numbers)
    answer = 0
    for number in numbers:
        print(number[0])
        if len(number) == 1:
            answer += (int(number[0]) * 10) + int(number[0])
            continue
        if len(number) > 1:
            answer += (int(number[0]) * 10) + int(number[-1])
            print(answer)
            continue
    print(answer)


if __name__ == "__main__":
    main()
