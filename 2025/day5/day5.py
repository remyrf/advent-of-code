with open("input.txt") as f:
    ranges_str, ingredients_str = f.read().split("\n\n")

ranges = []
for line in ranges_str.splitlines():
    start, end = line.split("-")
    ranges.append([int(start), int(end)])


def part_1():
    total = 0
    for ingredient_str in ingredients_str.splitlines():
        ingredient = int(ingredient_str)
        for start, end in ranges:
            if start <= ingredient <= end:
                total += 1
                break

    print(total)


def part_2():
    ranges_cpy = ranges.copy()
    non_overlapping = set()
    for r in ranges_cpy:
        if r is None:
            continue

        start, end = r

        while True:
            found_overlapping = False
            for y, o in enumerate(ranges_cpy):
                if o is None:
                    continue

                other_start, other_end = o

                if (
                    start <= other_start <= end
                    or start <= other_end <= end
                    or other_start <= start <= end <= other_end
                ):
                    found_overlapping = True
                    ranges_cpy[y] = None
                    start = min(start, other_start)
                    end = max(end, other_end)

            if not found_overlapping:
                break

        non_overlapping.add((start, end))

    total = 0
    for start, end in non_overlapping:
        total += end - start + 1

    print(total)


part_1()
part_2()
