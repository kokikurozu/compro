def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

ans = 0
N = int(input())
if N % 2 == 1:
    N *= 2
    cnt = 0
    for i in make_divisors(N):
        if i % 2 == 1:
            cnt += 1
    ans = cnt * 2
else:
    cnt = 0
    for i in make_divisors(N):
        if i % 2 == 1:
            cnt += 1
    ans = cnt * 2
print(ans)