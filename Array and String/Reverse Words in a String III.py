s = "Let's take LeetCode contest"

words = s.split()

for i in range(len(words)):
    words[i] = words[i][::-1]
        
print(' '.join(words))