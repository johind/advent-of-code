import re


def solve_part_one(lines: list[str]) -> int:
    """
    --- Day 1: Trebuchet?! ---

    As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

    The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

    For example:

    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet

    In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

    Consider your entire calibration document. What is the sum of all of the calibration values?

    """

    def find_digits(line: str) -> list[str]:
        return [char for char in line if char.isdigit()]

    values: list[int] = []

    for line in lines:
        numbers = find_digits(line)

        coordinate = int(numbers[0] + numbers[-1])
        values.append(coordinate)

    return sum(values)


def solve_part_two(lines: list[str]) -> int:
    """
    --- Part Two ---

    Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

    Equipped with this new information, you now need to find the real first and last digit on each line. For example:

    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen

    In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

    What is the sum of all of the calibration values?

    """
    number_pairs = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    values: list[int] = []

    # example: eightwo has to be split in 'eight' and 'two'

    pattern = re.compile("|".join([word for word in number_pairs.keys()] + [r"\d"]))

    for line in lines:
        matches = re.findall(pattern, line)

        first_occurrence = matches[0]
        last_occurrence = matches[-1]

        first_numer = number_pairs.get(first_occurrence, first_occurrence)
        last_number = number_pairs.get(last_occurrence, last_occurrence)

        coordinate = int(first_numer + last_number)
        values.append(coordinate)

    return sum(values)


def main():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    sol_one = solve_part_one(lines)
    sol_two = solve_part_two(lines)

    print("Advent of Code 2023, Day 1")
    print("Part One:", sol_one)
    print("Part Two:", sol_two)


if __name__ == "__main__":
    main()
