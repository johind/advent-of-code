import math
import re


def solve_part_one_brute_force(races):
    working_ways = []
    for max_time, top_distance in races:
        working_seconds = []
        # ignore 0 seconds and max seconds as travel speed
        for ms in range(1, max_time):
            if top_distance < (max_time - ms) * ms:
                working_seconds.append(ms)

        working_ways.append(len(working_seconds))

    return math.prod(working_ways)


def find_number_of_working_seconds(max_time: int, top_distance: int):
    """
    (max_time - ms) * ms > top_distance
    => -ms^2 + max_time * ms > top_distance
    => ms^2 - max_time * ms < -top_distance
    => ms^2 - max_time * ms + top_distance < 0
    """

    discriminant = max_time**2 - 4 * top_distance

    if discriminant >= 0:
        sqD = math.sqrt(discriminant)
        epsilon = math.nextafter(0, 1)

        root1 = (-max_time - sqD) / (-2)
        root2 = (-max_time + sqD) / (-2)

        return math.floor(root1 - epsilon) - math.ceil(root2 + epsilon) + 1
    else:
        return 0


def solve_part_one(races):
    ways = [
        find_number_of_working_seconds(max_time, top_distance)
        for max_time, top_distance in races
    ]
    return math.prod(ways)


def solve_part_two(max_times: list[int], top_distances: list[int]):
    max_time = int("".join(str(n) for n in max_times))
    top_distance = int("".join(str(n) for n in top_distances))

    return find_number_of_working_seconds(max_time, top_distance)


def main():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    pattern = re.compile(r"\d+")

    max_times = [int(n) for n in pattern.findall(lines[0])]
    top_distances = [int(n) for n in pattern.findall(lines[1])]

    sol_one = solve_part_one(zip(max_times, top_distances))
    sol_two = solve_part_two(max_times, top_distances)

    print("Solution Part 1:", sol_one)
    print("Solution Part 2:", sol_two)


if __name__ == "__main__":
    main()
