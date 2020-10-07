N, K = map(int, input().split())
if N < K:
    print(min(K - N, N))
else:
    print(min(N % K, K - (N % K)))