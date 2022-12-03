import string

import pytest


def parse_input(text):
    return text.split("\n")


def split_into_compartments(text):
    return [text[: len(text) // 2], text[len(text) // 2 :]]


def find_common_item_type(compartments):
    return "".join(set(compartments[0]).intersection(compartments[1]))


def item_type_value(item_type):
    if item_type.islower():
        return string.ascii_lowercase.index(item_type) + 1
    else:
        return string.ascii_uppercase.index(item_type) + 27

def part_one():
    with open("input.txt") as file:
        file_content = file.read().strip()
        total = 0
        for line in file_content.split("\n"):
            compartments = split_into_compartments(line)
            common_item_type = find_common_item_type(compartments)
            total += item_type_value(common_item_type)
    print(total)

if __name__ == "__main__":
    part_one()

@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ("A Y\nB X\nC Z", ["A Y", "B X", "C Z"]),
        ("1\n2\n3", ["1", "2", "3"]),
    ],
)
def test_parse_input(input, expected):
    assert parse_input(input) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ("Alyssa", ["Aly", "ssa"]),
    ],
)
def test_split_into_compartments(input, expected):
    assert split_into_compartments(input) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (["abc", "bfg"], "b"),
        (["jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"], "L"),
    ],
)
def test_split_into_compartments(input, expected):
    assert find_common_item_type(input) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ("a", 1),
        ("z", 26),
        ("A", 27),
        ("Z", 52),
    ],
)
def test_item_type_value(input, expected):
    assert item_type_value(input) == expected
