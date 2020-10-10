N = int(input())
cnt = 0
for A in range(1, N, 1):
    for B in range(1, N, 1):
        if A * B < N:
            cnt += 1
        else:
            break

print(cnt)
