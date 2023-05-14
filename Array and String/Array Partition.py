nums = [6,2,6,5,1,2]

sorted_nums = sorted(nums)

result = 0
for i in range(len(nums) - 1, 0, -2):
    result += sorted_nums[i-1]

return result