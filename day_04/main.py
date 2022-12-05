with open("input.txt") as file:
    file_content = file.read().strip()

    pairs = file_content.split()

    total_all_overlap = 0
    total_overlap = 0
    for pair in pairs:
        a, b, x, y = map(int, pair.replace(",", "-").split("-"))

        first_pair_numbers = set(range(a, b + 1))
        second_pair_numbers = set(range(x, y + 1))

        if (
            first_pair_numbers <= second_pair_numbers
            or second_pair_numbers <= first_pair_numbers
        ):
            total_all_overlap += 1

        if bool(first_pair_numbers & second_pair_numbers):
            total_overlap += 1

    print(total_all_overlap)
    print(total_overlap)
