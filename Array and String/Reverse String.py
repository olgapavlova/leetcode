str = ["h","e","l","l","o"]

first = 0
last = len(str) - 1

while first < last:
    str[first], str[last] = str[last], str[first]
    first += 1
    last -= 1

print(str)

