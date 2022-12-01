def part_one(calories_per_elf):
    most = 0
    for rations in calories_per_elf:
        if most < sum(rations):
            most = sum(rations)

    return most


def part_two(calories_per_elf):
    sorted_calories_per_elf = sorted(calories_per_elf, reverse=True, key=sum)

    top_three_elves = sorted_calories_per_elf[:3]
    calories_of_each_elf = list(map(sum, top_three_elves))
    calories_of_top_three_elves = sum(calories_of_each_elf)

    return calories_of_top_three_elves


def get_calories_per_elf(filename):
    with open(filename) as file:
        file_content = file.read().strip()

        calories_per_elf = [
            list(map(int, line.split("\n"))) for line in file_content.split("\n\n")
        ]

        return calories_per_elf


calories_per_elf = get_calories_per_elf("input.txt")

print(part_one(calories_per_elf))
print(part_two(calories_per_elf))
