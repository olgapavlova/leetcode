flowerbed = [0]
n = 1

line = [0]
capacity = 0
for i in flowerbed:
    if i: line.append(0)
    else: line[-1] += 1


if len(line) > 2:
    capacity = sum([max(0, (i - 1) // 2) for i in line[1:-1]])
    if line[0] != 0: capacity += line[0] // 2
    if line[-1] != 0: capacity += line[-1] // 2
elif len(line) == 2:
    capacity = max(0, (line[0]) // 2) + max(0, (line[1]) // 2)
else: capacity = max(0, (line[0] + 1) // 2)

print(capacity)

print(line)
