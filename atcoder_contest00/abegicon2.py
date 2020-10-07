N = int(input())
K = list(map(int, input().split()))
count = 0

for m in range(N):
    for n in range(m+1, N):
        for l in range(n+1, N):
            if K[m] != K[n] and K[m] != K[l] and K[l] != K[n]:
                now_list = sorted([K[m], K[n], K[l]])
                if now_list[2] < now_list[0] + now_list[1]:
                    count += 1

print(count)