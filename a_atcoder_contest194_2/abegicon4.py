N,W = map(int,input().split())
STP=[list(map(int,input().split()))for _ in range(N)]
Time = [0 for i in range(2*(10**5)+1)]

Is_judge = 'Yes'
cnt = 0

#増減表みたいなのを作る
for i in STP:
    Time[i[0]] += i[2]
    Time[i[1]] -= i[2]

for j in Time:
    cnt += j
    if cnt > W:
        Is_judge = 'No'
        break

print(Is_judge)