import string

import pytest


def split_into_compartments(text):
    return [text[: len(text) // 2], text[len(text) // 2 :]]


def find_common_item_type(strings):
    return "".join(set.intersection(*map(set, strings)))


def item_type_value(item_type):
    if item_type.islower():
        return string.ascii_lowercase.index(item_type) + 1
    else:
        return string.ascii_uppercase.index(item_type) + 27


def part_one(lines):
    total = 0
    for line in lines:
        compartments = split_into_compartments(line)
        common_item_type = find_common_item_type(compartments)
        total += item_type_value(common_item_type)
    return total


def part_two(lines):
    total = 0
    rucksacks = []
    for idx, line in enumerate(lines):
        rucksacks.append(line)
        if (idx + 1) % 3 == 0:
            common_item_type = find_common_item_type(rucksacks)
            total += item_type_value(common_item_type)
            rucksacks.clear()
    return total


if __name__ == "__main__":
    with open("input.txt") as file:
        file_content = file.read().strip()
        lines = file_content.split("\n")
        print(part_one(lines))
        print(part_two(lines))


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
def test_find_common_item_type(input, expected):
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