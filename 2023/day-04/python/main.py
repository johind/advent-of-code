def parse_line(line: str):
    # Split the line into card_info and numbers
    card_info, numbers = line.split(":")

    # Extract card_number from card_info and normalize whitespace
    card_number = card_info.strip().split()[1]

    # Split winning_numbers and my_numbers, and convert them to lists of integers
    winning_numbers, my_numbers = [
        list(map(int, num_str.strip().split()))
        for num_str in numbers.strip().split("|")
    ]

    return {
        "card_number": card_number,
        "winning_numbers": winning_numbers,
        "my_numbers": my_numbers,
    }


def solve_part_one(lines: list[str]):
    points = []
    for line in lines:
        card = parse_line(line)
        matching = set(card["winning_numbers"]).intersection(card["my_numbers"])

        if len(matching) > 0:
            card_points = [2**index for index, _ in enumerate(matching)].pop()
            points.append(card_points)

    return sum(points)


def solve_part_two(lines: list[str]):
    # cards = {2: {"wins": 3, "copies": 2}}
    cards: dict[int, dict] = {}

    for line in lines:
        card = parse_line(line)
        card_number = int(card["card_number"])
        matching = set(card["winning_numbers"]).intersection(card["my_numbers"])

        wins = len(matching)

        if cards.get(card_number):
            cards[card_number]["wins"] = wins
        else:
            cards[card_number] = {"wins": wins}

        copies = cards[card_number].get("copies", 0)

        # create as many copies as wins
        for i in range(1, wins + 1):
            if cards.get(card_number + i):
                cards[card_number + i]["copies"] += copies + 1
            else:
                cards[card_number + i] = {"copies": copies + 1}

    scratchcards_list = [entry.get("copies", 0) + 1 for entry in cards.values()]

    return sum(scratchcards_list)


def main():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    sol_one = solve_part_one(lines)
    sol_two = solve_part_two(lines)

    print("Solution Part 1:", sol_one)
    print("Solution Part 2:", sol_two)


if __name__ == "__main__":
    main()
