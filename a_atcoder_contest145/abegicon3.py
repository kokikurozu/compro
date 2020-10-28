N = int(input())
people_list = []
for i in range(N):
    A = int(input())
    xy=list([list(map(int,input().split()))for _ in range(A)])
    people_list += xy
max_num = 0

for i in range(2**N):
    ls = [1]*N
    for j in range(len(ls)):
        if (i >> j) & 1:
            ls[j] = 0
    for k in range(N):
        if ls[k] == 1:
            for l in people_list:
                for m in l:
                    if m[1] != ls[m[0]-1]:
                        break
                else:
                    continue
                break
        max_num = max(sum(ls),max_num)
print(max_num)