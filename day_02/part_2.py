from shutil import move

import pytest

shape = {
    "A": 1,
    "B": 2,
    "C": 3,
}

loses = {"A": "C", "B": "A", "C": "B"}
wins = {"A": "B", "B": "C", "C": "A"}

outcome = {"lost": 0, "draw": 3, "won": 6}


def parse_input(text):
    text = text.split("\n")
    return [[x for x in item.split(" ")] for item in text]


def score_part2(strategy):
    score = 0
    for move in strategy:
        their_move, my_move = move

        score += shape[their_move] + outcome["draw"] if my_move == "Y" else 0
        score += shape[loses[their_move]] + outcome["lost"] if my_move == "X" else 0
        score += shape[wins[their_move]] + outcome["won"] if my_move == "Z" else 0

    return score


if __name__ == "__main__":
    with open("input.txt") as file:
        strategy = parse_input(file.read().strip())
        print(score_part2(strategy))
