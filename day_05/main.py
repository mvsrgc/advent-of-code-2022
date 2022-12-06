# col1 = [val[1] for val in new]
# col2 = [val[5] for val in new]
# etc.


def part_one(cargo, moves):
    columns = cargo

    for move in moves:
        num_crates, source, dest = [int(x) for x in move.split(" ") if x.isdigit()]
        for _ in range(num_crates):
            crate = columns[source].pop(0)
            columns[dest].insert(0, crate)

    for key, val in enumerate(columns.items()):
        print(key, val)


def part_two(cargo, moves):
    columns = cargo

    for move in moves:
        num_crates, source, dest = [int(x) for x in move.split(" ") if x.isdigit()]
        intermediary = []
        for _ in range(num_crates):
            crate = columns[source].pop(0)
            intermediary.append(crate)
        columns[dest][0:0] = intermediary

    for key, val in enumerate(columns.items()):
        print(key, val)


if __name__ == "__main__":
    with open("input.txt") as file:
        cargo, moves = file.read().split("\n 1   2   3   4   5   6   7   8   9 \n\n")
        cargo = [line for line in cargo.splitlines()]
        moves = [move for move in moves.splitlines()]

        columns = dict()
        col = 1
        for i in range(1, 34, 4):
            columns[col] = [line[i] for line in cargo if line[i].isalpha()]
            col += 1

        # part_one(columns, moves)
        part_two(columns, moves)
