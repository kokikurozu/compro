K = int(input())
A = [1,2,3,4,5,6,7,8,9] + [0] * 10 * K
i = 9
j = 0
while i < K:
    if A[j] % 10 != 0:
        A[i] = 10 * A[j] + A[j] % 10 - 1; i += 1
    A[i] = 10 * A[j] + A[j] % 10; i += 1
    if A[j] != 9:
        A[i] = 10 * A[j] + A[j] % 10 + 1; i += 1
    j += 1
print(A[K - 1])