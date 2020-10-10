N = int(input())
int_list = list(map(int,input().split()))
flag_list = [0] * (max(int_list) + 1)
i = 0

for j in int_list:
    flag_list[j] = 1
    while flag_list[i]:
        i += 1
    print(i)
