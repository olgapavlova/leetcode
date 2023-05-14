numbers = [12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997]
target = 542

i1 = 0
i2 = len(numbers) - 1
found = False

while (not found):
    if i1 % 2 == 0:
        while ((numbers[i1] + numbers[i2] > target) and (i2 > i1 + 1)): i2 -= 1
    else:
        while ((numbers[i1] + numbers[i2] < target) and (i2 < len(numbers) - 1)): i2 += 1

    print(i1, i2, numbers[i1] + numbers[i2], numbers[i1] + numbers[i2] > target)

    if (numbers[i1] + numbers[i2] == target):
        found = True
    else:
        i1 += 1
        if i1 == i2: i2 +=1
        print(i1, i2)

print([i1 + 1, i2 + 1])