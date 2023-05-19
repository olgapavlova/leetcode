rowIndex = 1

line = [1]
for i in range(rowIndex):
    for j in range(len(line) - 1, 0, -1):
        line[j] += line[j-1]
        print(f"j: {j}, line[j]: {line[j]}")
    line.append(1)

print(line)
