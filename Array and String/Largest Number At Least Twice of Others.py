nums = [3,6,1,0]
if nums[0] <= nums[1]:
    max_index = 1
    second_index = 0
else:
    max_index = 0
    second_index = 1

for i in range(2, len(nums)):
    if nums[i] > nums[max_index]:
        second_index = max_index
        max_index = i
    else:
        if nums[i] > nums[second_index]:
            second_index = i

if nums[max_index] >= 2 * nums[second_index]:
    print(max_index)
else: print(-1)