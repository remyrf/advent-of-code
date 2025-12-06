from collections import defaultdict

with open("input.txt") as f:
    lines = f.read().splitlines()


def part_1():
    nums = defaultdict(list)

    for line in lines[:-1]:
        for x, w in enumerate(line.split()):
            nums[x].append(int(w))

    total = 0
    for x, op in enumerate(lines[-1].split()):
        if op == "*":
            a = 1
            for num in nums[x]:
                a *= num
            total += a
        else:
            total += sum(nums[x])

    print(total)


def part_2():
    nums = defaultdict(str)

    for line in lines[:-1]:
        for x, char in list(enumerate(line))[::-1]:
            nums[x] += char

    nums = [v[1] for v in sorted(nums.items(), key=lambda x: -x[0])][::-1]

    groups = []
    group = []
    for num in nums:
        if num.isspace():
            groups.append(group)
            group = []
        else:
            group.append(int(num))
    groups.append(group)

    total = 0
    for x, op in enumerate(lines[-1].split()):
        if op == "*":
            a = 1
            for num in groups[x]:
                a *= num
            total += a
        else:
            total += sum(groups[x])

    print(total)


part_2()
