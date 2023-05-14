a = "1010"
b = "1011"

aa = [int(c) for c in a][::-1]
bb = [int(c) for c in b][::-1]
result = [0 for _ in range(max([len(aa), len(bb)]))]

shift = 0
for i in range(min([len(aa), len(bb)])):
    result[i] = aa[i] + bb[i] + shift
    print(i, aa[i], bb[i], shift, result[i])
    if result[i] > 1:
        shift = 1
        result[i] = result[i] % 2
    else: shift = 0

if len(aa) > len(bb):
    c = aa
elif len(aa) < len(bb):
    c = bb
else:
    True

for i in range(min([len(aa), len(bb)]), max([len(aa), len(bb)])):
    result[i] = c[i] + shift
    print(i, result[i])
    if result[i] > 1:
        shift = 1
        result[i] = result[i] % 2
    else: shift = 0

if shift == 1: result.append(1)

result_string = ''.join([str(i) for i in result[::-1]])

print(result_string)