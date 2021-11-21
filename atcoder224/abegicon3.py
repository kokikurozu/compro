n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
count = 0
for i in range(n):
    for j in range(i,n):
        for k in range(j,n):
            if abs((s[i][0]-s[k][0]) * (s[j][1] - s[k][1]) - (s[j][0] - s[k][0]) * (s[i][1] - s[k][1])) > 0:
                count += 1

print(count)