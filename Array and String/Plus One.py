digits = [9]
digiverse = digits[::-1]
digiverse.append(0)

shift_num = 1
i = 0
while shift_num:
    digiverse[i] += shift_num
    if digiverse[i] == 10:
        digiverse[i] = 0
        shift_num = 1
    else: shift_num = 0
    i += 1

if digiverse[-1] == 0: digiverse.pop()

digits = digiverse[::-1]

print(digits)