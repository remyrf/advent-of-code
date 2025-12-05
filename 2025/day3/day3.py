with open("input.txt") as f:
    puzzle_input = f.read()

total = 0
for line in puzzle_input.splitlines():
    nums = [int(x) for x in line]
    final_num = 0

    prev_biggest = -1
    for x in range(1, 13):
        biggest = prev_biggest + 1
        for y in range(biggest, x + len(nums) - 12):
            if nums[y] > nums[biggest]:
                biggest = y

        final_num += 10 ** (12 - x) * nums[biggest]
        prev_biggest = biggest

    total += final_num

print(total)
