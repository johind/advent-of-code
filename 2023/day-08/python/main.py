import itertools
import math
import re


def solve_part_one(directions: list[int], data: dict[str, tuple[int, int]]):
    key = "AAA"

    steps = 0
    for direction in itertools.cycle(directions):
        steps = steps + 1
        key = data[key][direction]

        if key == "ZZZ":
            break

    return steps


def solve_part_two(directions: list[int], data: dict[str, tuple[int, int]]):
    def solve_steps():
        pass
    r = 1
    for key in data:
        if key.endswith("A"):
            r = math.lcm(r, solve_steps(key))



""" def solvesteps(start):
	pos = start
	idx = 0
	while not pos.endswith('Z'):
		d = directions[idx%len(directions)]
		pos = conn[pos][0 if d=='L' else 1]
		idx += 1
	return idx
ret = 1
for start in conn:
	if start.endswith('A'):
		ret = math.lcm(ret, solvesteps(start))
print("p2", ret) """


def main():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    # left = 0, right = 1
    directions = [int(n == "R") for n in lines[0]]
    # directions = map(convert_direction, list(lines[0]))
    # directions = list(map(lambda n: int(n == "R"), lines[0]))
    pattern = re.compile(r"[A-Z0-9]+")

    data = {}

    for line in lines[2:]:
        matches = pattern.findall(line)

        # Create a dictionary and append it to the result list
        data[matches[0]] = (matches[1], matches[2])

    sol_one = solve_part_one(directions, data)

    print("Solution Part 1:", sol_one)


if __name__ == "__main__":
    main()
