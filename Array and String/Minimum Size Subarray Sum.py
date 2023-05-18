nums = [2,3,1,2,4,3]
target = 7

i2 = 0
s = nums[i2]
minlen = len(nums)

for i1 in range(len(nums)):
    if i1 > 0: s -= nums[i1 - 1]

    if i1 == i2 + 1:
        s += nums[i2]
        i2 = i1

    print(i1, i2, '--', s)

    if (s < target):
        while (s < target) and (i2 < len(nums) - 1):
            i2 += 1
            s += nums[i2]
            print(i1, i2, '-', s)
    else:
        while (s > target) and (i2 >= i1):
            s -= nums[i2]
            print(i1, i2, '-', s)
            i2 -= 1
        i2 += 1
        s += nums[i2]

    if (s >= target): minlen = min(minlen, i2 - i1 + 1)
    print(minlen)

print(i1, i2, s)
