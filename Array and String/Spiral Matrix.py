matrix = [[7],[9],[6]]

result = []

while len(matrix) > 0:
    result.extend(matrix.pop(0))
    len(matrix) == 0 or result.extend([l.pop() for l in matrix])
    for l in range(len(matrix)-1, -1, -1):
        if matrix[l] == []: matrix.pop(l)
     
    len(matrix) == 0 or result.extend(matrix.pop()[::-1])
    len(matrix) == 0 or result.extend([l.pop(0) for l in matrix][::-1])
    for l in range(len(matrix)-1, -1, -1):
        if len(matrix[l]) == 0: matrix.pop(l)

print(result)
