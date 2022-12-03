import pytest

shape = {
    "X": 1,
    "A": 1,
    "Y": 2,
    "B": 2,
    "Z": 3,
    "C": 3,
}

# key beats shapes in values
beats = {"X": "C", "Y": "A", "Z": "B"}

outcome = {"lost": 0, "draw": 3, "won": 6}


def parse_input(text):
    text = text.split("\n")
    return [[x for x in item.split(" ")] for item in text]


def score_part1(strategy):
    score = 0
    for move in strategy:
        their_move, my_move = move

        score += outcome["draw"] if shape[their_move] == shape[my_move] else 0
        score += outcome["won"] if their_move == beats[my_move] else 0
        score += shape[my_move]

    return score


if __name__ == "__main__":
    with open("input.txt") as file:
        strategy = parse_input(file.read().strip())
        print(score_part1(strategy))


@pytest.mark.parametrize(
    ("input", "expected"),
    (("A A\nB B\nC C", [["A", "A"], ["B", "B"], ["C", "C"]]),),
)
def test_parse_input(input, expected):
    assert parse_input(input) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    [("A Y\nB X\nC Z", 15)],
)
def test_score_part1(input, expected):
    assert score_part1(parse_input(input)) == expected
