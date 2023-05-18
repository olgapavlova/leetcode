numbers = [-10,-8,-2,1,2,5,6]
target = 0

i1 = 0
i2 = len(numbers)
found = False

shift = [0, -1]
current = -9_999_999

while (not found):
    i1 += shift[0]
    i2 += shift[1]
    current = numbers[i1] + numbers[i2]

    shift_next = shift.copy()

    if current == target: found = True

    # Ideal next shift
    if (current < target) & (shift == [0, -1]): shift_next = [1, 0]
    if (current > target) & (shift == [0, 1]): shift_next = [1, 0]
    
    if (current > target) & (shift == [1, 0]): shift_next = [0, -1]
    if (current < target) & (shift == [1, 0]): shift_next = [0, 1]

    # Correction
    if i2 == i1 + 1: shift_next = [0, 1]
    if (i2 == len(numbers) - 1) & (shift_next[1] == 1): shift_next = [1, 0]

    print(i1, i2, shift, shift_next, last, current)
    shift = shift_next.copy()

print([i1 + 1, i2 + 1])
