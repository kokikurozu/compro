N = int(input())
xy=[list(map(int,input().split()))for _ in range(N)]
Is_judge = 'No'
for i in range(N):
    for j in range(i+1, N, 1):
        for k in range(j+1, N ,1):
            dx1 = xy[i][0] - xy[j][0]
            dy1 = xy[i][1] - xy[j][1]
            dx2 = xy[i][0] - xy[k][0]
            dy2 = xy[i][1] - xy[k][1]
            if (dx2 * dy1) == (dx1 * dy2):
                Is_judge = 'Yes'
                break
        else:
            continue
        break
    else:
        continue
    break

print(Is_judge)