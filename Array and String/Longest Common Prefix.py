strs = ["flower","flow","flight"]

max_prefix_len = min([len(l) for l in strs])

max_prefix = ""
for i in range(max_prefix_len + 1):
    if all([l[:i] == strs[0][:i] for l in strs]):
        print([l[:i] == strs[0][:i] for l in strs])
        max_prefix = strs[0][:i]