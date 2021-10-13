s = list(input())
j = [0 for i in range(len(s))]
for i in range(len(s)):
    j[i] = int(s[i])
ans10 = 0
ans01 = 0
for i in range(len(j)):
    if i % 2 == j[i]:
        ans10 += 1
    if (i+1) % 2 == j[i]:
        ans01 += 1
print(min(ans01,ans10))