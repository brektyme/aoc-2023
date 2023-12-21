import re
from functools import reduce
from pathlib import Path

import libs

card_filter = re.compile(r"^Card\s+[\d]+:\s*((?:(\d*)\s?)+?)\|")

card_win_num_filter = re.compile(f".*\|\s*((?:(\d*)\s?)+?)$")


def main():
    cards = libs.get_input(Path("input.txt"))
    matches = []
    for card in cards:
        # print(card_filter.findall(card))
        card_nums = card_filter.findall(card)[0][0].split()
        print(card_nums)
        win_nums = card_win_num_filter.findall(card)[0][0].split()
        print(win_nums)
        match = list(set(card_nums) & set(win_nums))
        matches.append(match) if len(match) > 0 else None
    print(matches)
    answer = reduce(lambda x, y: x + y, [pow(2, len(match) - 1) for match in matches])
    print(f"answer: {answer}")


if __name__ == "__main__":
    main()
