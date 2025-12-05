with open("input.txt") as f:
    grid = [list(l) for l in f.read().splitlines()]

adj8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

total = 0
while True:
    changed = False

    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char == ".":
                continue

            neighbours = 0

            for x, y in adj8:
                new_x, new_y = row + x, col + y
                if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(line):
                    continue

                if grid[new_x][new_y] == "@":
                    neighbours += 1

            if neighbours < 4:
                total += 1
                changed = True
                grid[row][col] = "."

    if not changed:
        break

print(total)
