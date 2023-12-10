from collections import Counter


def main():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    for line in lines:
        val_1, val_2 = line.strip().split()

        print(val_1)


def classify_hand(cards: str):
    # Count the occurrences of each card label
    card_counts = Counter(cards)

    # Sort the cards based on their counts and labels
    sorted_cards = sorted(card_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)

    # Extract counts and labels
    counts, labels = zip(*sorted_cards)

    # Five of a kind
    if counts[0] == 5:
        return "Five of a kind"

    # Four of a kind
    elif counts[0] == 4 and counts[1] == 1:
        return "Four of a kind"

    # Full house
    elif counts[0] == 3 and counts[1] == 2:
        return "Full house"

    # Three of a kind
    elif counts[0] == 3 and counts[1] == 1 and counts[2] == 1:
        return "Three of a kind"

    # Two pair
    elif counts[0] == 2 and counts[1] == 2 and counts[2] == 1:
        return "Two pair"

    # One pair
    elif counts[0] == 2 and counts[1] == 1 and counts[2] == 1 and counts[3] == 1:
        return "One pair"

    # High card
    else:
        return "High card"


def solve_part_one(line: str):
    pass


# https://www.reddit.com/r/adventofcode/comments/18csyvh/2023_day_7_part_1_python_ridiculously_short/


if __name__ == "__main__":
    main()
