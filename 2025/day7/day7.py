from functools import cache

with open("input.txt") as f:
    lines = f.read().splitlines()

start = (0, 0)
splitters = set()

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == "S":
            start = (row, col)
        if char == "^":
            splitters.add((row, col))


def part_1():
    beams = {start}
    splits = 0
    for _ in lines:
        next_beams = set()
        for br, bc in beams:
            if (br + 1, bc) in splitters:
                next_beams.add((br + 1, bc - 1))
                next_beams.add((br + 1, bc + 1))
                splits += 1
            else:
                next_beams.add((br + 1, bc))
        beams = next_beams

    print(splits)


def part_2():
    @cache
    def extend_beam(point, n=0):
        while point not in splitters:
            r, c = point
            point = (r + 1, c)
            if point[0] >= len(lines):
                return n + 1

        r, c = point
        return extend_beam((r, c - 1), n) + extend_beam((r, c + 1), n)

    print(extend_beam(start))


part_1()
part_2()
