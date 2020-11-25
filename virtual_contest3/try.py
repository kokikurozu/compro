for i in range(2**N):
    ls = [1]*N
    for j in range(len(ls)):
        if (i >> j) & 1:
            ls[j] = 0
            Is_judge = 1
            for j in range(N):
                if ls[j] == 1:
                    for k in xy_list[j]:
                        if ls[k[0]] != k[1]:
                            Is_judge = 0
        if Is_judge == 1:
            max_now = max(max_now,sum(ls))
print(max_now)