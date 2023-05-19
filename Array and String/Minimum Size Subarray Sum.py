nums = [10,2,3]
target = 6

i2 = 0
current = 0
dir = 1
minsum = []

for i1 in range(len(nums)):
    result = 'looking'

    if (i1 <= i2):
        if (i1 > 0): current -= nums[i1 - 1] # был сдвиг — надо вычесть
        else: current = nums[0] # первый пункт — сдвига не было
    else:
        if (i2 < len(nums) - 1):
            i2 += 1 # оба указателя только что указывали на одну точку — должны продолжать
            current = nums[i2] # сумма — это значение в точке 
        else: result = 'fail'

    if current == target:
        result = 'found' # TODO Check necessity
        minsum.append(i2 - i1 + 1)

    if (current > target) and (i2 == i1):
        result = 'found' # TODO Check necessity
        minsum.append(1)

    if current < target:
        # print('Вверх')
        dir = 1
    if current > target:
        # print('Вниз')
        dir = -1

    print(f"= i1 = {i1}, i2 = {i2}, current = {current}, result = {result}, dir = {dir}")

    while result == 'looking':
        i2 += dir
        # print(f"— — i2 = {i2}, dir = {dir}")

        if (i1 <= i2) and (i2 < len(nums)):
            if dir == 1: current += nums[i2]
            elif i2 < len(nums) - 1: current -= nums[i2 + 1]

            if (dir == -1) and (current < target):
                result = 'found'
                minsum.append(i2 - i1 + 2)
            
            if (dir == 1) and (current > target):
                result = 'found'
                minsum.append(i2 - i1 + 1)
            
            if (current == target):
                result = 'found'
                minsum.append(i2 - i1 + 1)

            print(f"• i1 = {i1}, i2 = {i2}, current = {current}, result = {result}")

        else:
            result = 'fail'
            i2 -= dir

print(minsum)

