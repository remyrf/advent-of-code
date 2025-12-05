with open("input.txt", "r") as f:
    cards_lines = f.readlines()


def part_1():
    total = 0
    for line in cards_lines:
        _, nums = line.split(": ")
        left, right = nums.split("|")

        winning_nums = [int(x) for x in left.split()]
        chosen_nums = [int(x) for x in right.split()]

        wins = sum(1 if x in winning_nums else 0 for x in chosen_nums)
        total += 2 ** (wins - 1) if wins > 0 else 0

    print(total)


def part_2():
    cards = []

    for line in cards_lines:
        label, nums = line.split(": ")
        card_num = int(label[4:])
        left, right = nums.split("|")

        winning_nums = [int(x) for x in left.split()]
        chosen_nums = [int(x) for x in right.split()]

        wins = sum(1 if x in winning_nums else 0 for x in chosen_nums)

        cards.append((card_num, wins))

    og_cards = {k: v for k, v in cards}

    total_cards = [*cards]
    while len(cards) > 0:
        next_cards = []
        for card in cards:
            for x in range(card[0] + 1, card[0] + card[1] + 1):
                next_cards.append((x, og_cards[x]))

        total_cards.extend(next_cards)
        cards = next_cards

    print(len(total_cards))


print("Part 1:")
part_1()

print("Part 2:")
part_2()
