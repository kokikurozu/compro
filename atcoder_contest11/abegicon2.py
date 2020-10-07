A, B, C, K = map(int, input().split())
lista = [for [0,0] i in range(N)]
if K <= A:
    print(K)
elif A <= K <= A + B:
    print(A)
else:
    print(A - (K - (A + B)))