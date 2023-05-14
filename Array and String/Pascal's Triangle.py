numRows = 2

result = [[1]]
for i in range(numRows-1):
    line = [1,1]
    for j in range(1, len(result[-1])):
        line.insert(j, result[-1][j-1] + result[-1][j])
    print(line)
    result.append(line)

print(result)
