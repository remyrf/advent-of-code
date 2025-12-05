with open("input.txt") as f:
    lines = f.readlines()

num = 50
times = 0
for line in lines:
    dir = line[0]
    dist = int(line[1:])

    for x in range(dist):
        if dir == "L":
            num -= 1
        else:
            num += 1

        if num < 0:
            num = 99
        if num > 99:
            num = 0

        if num == 0:
            times += 1


print(times)
