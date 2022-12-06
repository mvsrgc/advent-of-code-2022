import pytest


def main(text, num_chars):
    for i, _ in enumerate(text):
        vals = text[i:i+num_chars]
        if len(set(vals)) == num_chars:
            return text.index(vals) + num_chars

if __name__ == "__main__":
    with open("input.txt") as file:
        file_content = file.read().strip()

        print(main(file_content, 4))
        print(main(file_content, 14))


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test(input, expected):
    assert main(input, 4) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
    ],
)
def test_two(input, expected):
    assert main(input, 14) == expected
