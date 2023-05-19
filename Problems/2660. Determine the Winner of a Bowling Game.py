player1 = [4,10,7,9]
player2 = [6,5,2,3]

check = lambda i, p: ((i==1) and (p[i-1] == 10)) or ((i >= 2) and ((p[i-2] == 10) or (p[i-1] == 10)))

p1_vals = [player1[i] * (1 + check(i, player1)) for i in range(len(player1))]
p2_vals = [player2[i] * (1 + check(i, player2)) for i in range(len(player2))]

diff = sum(p1_vals) - sum(p2_vals)
if diff == 0: print(0)
elif diff < 0: print(2)
else: print(1)