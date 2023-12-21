import re
from pathlib import Path
from typing import List, Tuple, Dict, Union

import libs

card_nums_filter = re.compile(r"^Card\s+(\d+):\s*((?:(\d*)\s?)+?)\|")
card_win_num_filter = re.compile(r".*\|\s*((?:(\d*)\s?)+?)$")


def filter_card(card: str) -> Tuple[int, List[int], List[int], List[int]]:
    card_num, card_nums, _ = card_nums_filter.findall(card)[0]
    card_nums = card_nums.split()
    win_nums = card_win_num_filter.findall(card)[0][0].split()
    match = list(set(card_nums) & set(win_nums))
    return int(card_num), card_nums, win_nums, match


def get_child_cards(
    card_num: int,
    num_matches: int,
    cards: List[Dict[str, List[int]]],
) -> Union[List[Dict[str, List[int]]], Dict[str, List[int]]]:
    if num_matches:
        children = []
        for i in range(card_num + 1, card_num + num_matches + 1):
            children.extend(
                get_child_cards(
                    card_num=i,
                    num_matches=len(cards[i]["match"]),
                    cards=cards,
                )
            )
        children.append(cards[card_num])
        return children
    else:
        return [cards[card_num]]


def main():
    cards = libs.get_input(Path("input.txt"))
    cards_filtered = [{}] * (len(cards) + 1)
    for card in cards:
        card_num, card_nums, win_nums, match = filter_card(card)
        cards_filtered[int(card_num)] = {
            "card_num": int(card_num),
            "card_nums": card_nums,
            "win_nums": win_nums,
            "match": match,
        }
    total_cards = 0
    for i in range(1, len(cards_filtered)):
        child_cards = []
        child_cards.extend(
            get_child_cards(
                card_num=i,
                num_matches=len(cards_filtered[i]["match"]),
                cards=cards_filtered,
            )
        )
        total_cards += len(child_cards)
    print(f"answer: {total_cards}")


if __name__ == "__main__":
    main()
