mat = [[1,2],[3,4]]
rows = len(mat)
cols = len(mat[0])
size = rows + cols

sum = []
for i in range(rows):
    for j in range(cols):
        sum.append([i + j, i, j])

sum.sort(key=lambda x:x[0]*size + x[2 - (x[0] % 2)])

result = [mat[x[1]][x[2]] for x in sum]

print(result)