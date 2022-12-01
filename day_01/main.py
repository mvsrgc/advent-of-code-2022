def part_one(elf_calories):
    most = 0
    for elf in elf_calories:
        if most < sum(elf):
            most = sum(elf)

    return most


def part_two(elf_calories):
    sorted_elf_calories = sorted(elf_calories, reverse=True, key=sum)

    top_three_elves = sorted_elf_calories[:3]
    summed_elf_calories = list(map(sum, top_three_elves))
    total_calories_top_three_elves = sum(summed_elf_calories)

    return total_calories_top_three_elves


def get_elf_calories(filename):
    with open(filename) as file:
        file_content = file.read().strip()

        elf_calories = [
            list(map(int, line.split("\n"))) for line in file_content.split("\n\n")
        ]

        return elf_calories


elf_calories = get_elf_calories("input.txt")

print(part_one(elf_calories))
print(part_two(elf_calories))
