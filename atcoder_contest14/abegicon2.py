N = int(input())
*A, = map(int, input().split())
now = 1
if A.count(0) == 0:
    for i in A:
        now *= i
        if now > 10**18:
            now = -1
            break
else:
    now = 0
print(now)