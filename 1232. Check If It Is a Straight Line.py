coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]

coordinates.sort(key=lambda x: x[0])
dx0 = coordinates[1][0] - coordinates[0][0]
dy0 = coordinates[1][1] - coordinates[0][1]

for i in range(len(coordinates) - 1, 1, -1):
    dx = coordinates[i][0] - coordinates[0][0]
    dy = coordinates[i][1] - coordinates[0][1]

    if dx * dy0 != dx0 * dy: print(False)
    
print(True)