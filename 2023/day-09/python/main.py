def compute_differences(numbers: list[int]) -> list[int]:
    return [j - i for i, j in zip(numbers[:-1], numbers[1:])]


def extrapolate(numbers: list[int]) -> int:
    differences: list[int] = numbers

    last_numbers = []
    while any(differences):
        differences = compute_differences(differences)
        last_numbers.append(differences[-1])

    return numbers[-1] + sum(last_numbers)


def solve_part_one(lines: list[str]):
    extrapolated_numbers = []
    for line in lines:
        numbers = [int(n) for n in line.split()]

        extrapolated = extrapolate(numbers)

        extrapolated_numbers.append(extrapolated)

    return sum(extrapolated_numbers)


def solve_part_two(lines: list[str]):
    extrapolated_numbers = []
    for line in lines:
        numbers = [int(n) for n in line.split()][::-1]

        extrapolated = extrapolate(numbers)

        extrapolated_numbers.append(extrapolated)

    return sum(extrapolated_numbers)


def main():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    sol_one = solve_part_one(lines)
    sol_two = solve_part_two(lines)

    print("Solution Part 1:", sol_one)
    print("Solution Part 2:", sol_two)


if __name__ == "__main__":
    main()
