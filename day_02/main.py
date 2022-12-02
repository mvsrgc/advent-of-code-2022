import pytest

shape_score = {
    "X": 1,
    "A": 1,
    "Y": 2,
    "B": 2,
    "Z": 3,
    "C": 3,
}

beats = {"X": ("C"), "Y": ("A"), "Z": ("B")}

outcome_score = {"lost": 0, "draw": 3, "won": 6}


def parse_input(text):
    text = text.split("\n")
    return [[x for x in item.split(" ")] for item in text]


def score(strategy):
    score = 0
    for move in strategy:
        their_move = move[0]
        my_move = move[1]

        score += (
            outcome_score["draw"]
            if shape_score[their_move] == shape_score[my_move]
            else 0
        )
        score += outcome_score["won"] if their_move in beats[my_move] else 0
        score += shape_score[my_move]

    return score

if __name__ == "__main__":
    with open("input.txt") as file:
        strategy = parse_input(file.read().strip())
        print(score(strategy))


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
def test_score(input, expected):
    assert score(parse_input(input)) == expected
