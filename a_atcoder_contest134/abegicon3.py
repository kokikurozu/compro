N = int(input())
Ni = [0 for _ in range(N)]
for i in range(N):
    Ni[i] = int(input())

#ori_Ni = Ni

max_1 = max(Ni)
for i in range(N):
    if Ni[i] == max_1:
        Ni[i] = 0
        break
max_2 = max(Ni)


if max_1 == max_2:
    for i in range(N):
        print(max_1)
else:
    for i in range(N):
        if Ni[i] == 0:
            print(max_2)
        else:
            print(max_1)