N = int(input())
ci = list(str(input()))

cnt = 0
count_Red = ci.count('R')
for i in range(count_Red):
    if ci[i] == 'W':
        cnt += 1
print(cnt)