points = [[1,1],[2,3],[3,2]]

points.sort(key=lambda x: x[0])
print(points)
if (points[0] != points[1]) and (points[1] != points[2]) and (points[2] != points[0]):
    m1 = (points[1][0] - points[0][0]) * (points[2][1] - points[0][1])
    m2 = (points[2][0] - points[0][0]) * (points[1][1] - points[0][1])
    print(m1, m2, m1 != m2)
else: print(False)