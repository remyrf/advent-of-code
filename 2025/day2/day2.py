with open("input.txt") as f:
    puzzle_input = f.read()

ranges = puzzle_input.split(",")

total = 0

for r in ranges:
    start, end = r.split("-")
    start = int(start)
    end = int(end)

    for x in range(start, end + 1):
        num = str(x)
        for y in range(1, len(num) // 2 + 1):
            if (len(num) - y) / y % 1 != 0:
                continue

            sub = num[:y]
            if num[y:] == sub * ((len(num) - y) // y):
                total += x
                break

print(total)
