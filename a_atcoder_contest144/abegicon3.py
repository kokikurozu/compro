N = int(input())
for i in range(int(N ** 0.5), 0, -1):
    if N / i == N // i:
        break

move = (i - 1) + (N / i) - 1
print(int(move))