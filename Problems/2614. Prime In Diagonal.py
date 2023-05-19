nums = [[1,2,3],[5,6,7],[9,10,11]] 

maxresult = 0

def check_prime(number):
    p = True
    i = 2
    if number == 1: p = False
    while p and (i <= number/2):
        if (number % i == 0): p = False
        i += 1
    return p

for i in range(len(nums)):
    if (nums[i][i] > maxresult) and check_prime(nums[i][i]):
        maxresult = max(nums[i][i], maxresult)

    if (nums[i][len(nums) - i - 1] > maxresult) and check_prime(nums[i][len(nums) - i - 1]):
        maxresult = max(nums[i][len(nums) - i - 1], maxresult)

print(maxresult)