n = int(input())
ai = map(int,input().split())
cnt = [0 for i in range(n)]

for i in ai:
    cnt[i-1] += 1

for j in range(n):
    if cnt[j] == 3:
        print(j+1)
        break