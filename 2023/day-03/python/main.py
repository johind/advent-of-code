import math


def is_symbol(char: str):
    return 33 <= ord(char) <= 126 and char != "." and not char.isalnum()


def solve_part_one(lines: list[str]):
    part_numbers: list[int] = []

    for i, line in enumerate(lines):
        number = ""
        for j, char in enumerate(line):
            is_digit = False
            if char.isdigit():
                number += char
                is_digit = True

            if (number and not is_digit) or (is_digit and j == len(line) - 1):
                x_start = max(0, j - len(number) - 1)
                x_end = min(j + 1, len(line))
                y_start = max(0, i - 1)
                y_end = min(i + 2, len(lines))

                is_part_number = False

                for k in range(y_start, y_end):
                    for l in range(x_start, x_end):
                        if is_symbol(lines[k][l]):
                            is_part_number = True
                            part_numbers.append(int(number))
                            break

                    if is_part_number:
                        break

                number = ""

    # print(part_numbers)

    return sum(part_numbers)


def get_adjacent_symbol(
    lines: list[str], number: str, x_after: int, y: int
) -> tuple[int, int] | None:
    x_start = max(0, x_after - len(number) - 1)
    x_end = min(x_after + 1, len(lines[y]))
    y_start = max(0, y - 1)
    y_end = min(y + 2, len(lines))

    # print("START")

    for i in range(y_start, y_end):
        for j in range(x_start, x_end):
            # print(lines[i][j])
            if lines[i][j] == "*":
                return (i, j)

    return None


def solve_part_two(lines: list[str]) -> int:
    """
    The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

    This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

    Consider the same engine schematic again:

    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..

    In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

    What is the sum of all of the gear ratios in your engine schematic?
    """
    numbers_with_adjacent: dict[tuple, list[int]] = {}

    for y, line in enumerate(lines):
        buffer = ""
        for x, char in enumerate(line):
            is_digit = char.isdigit()
            is_last_char = x == len(line) - 1
            if is_digit:
                buffer += char
            if (not is_digit and buffer) or (is_digit and is_last_char):
                position = get_adjacent_symbol(lines, buffer, x, y)

                if position:
                    number = int(buffer)
                    if numbers_with_adjacent.get(position):
                        numbers_with_adjacent[position].append(number)
                    else:
                        numbers_with_adjacent[position] = [number]

                buffer = ""

    gear_ratios = []

    for _, value in numbers_with_adjacent.items():
        if len(value) == 2:
            gear_ratios.append(math.prod(value))

    return sum(gear_ratios)


def main():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

        sol_one = solve_part_one(lines)
        sol_two = solve_part_two(lines)

        print("Solution Part 1:", sol_one)
        print("Solution Part 2:", sol_two)


if __name__ == "__main__":
    main()
