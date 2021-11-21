n = int(input())
s = [list(map(int, input().split())) for _ in range(n-1)]
li = [0 for i in range(n)]
for i in range(n-1):
    li[s[i][0]-1] += 1
    li[s[i][1]-1] += 1
flg = 'Yes'
for k in li:
    if k != 1 and k != (n-1):
        flg = 'No'
        break

print(flg)