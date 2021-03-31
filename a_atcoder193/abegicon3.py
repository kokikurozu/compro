n = int(input())
ans = 0
a = set()

for i in range(2,10 ** 5 + 1,1):
    x = i*i
    while x <= n:
        a.add(x)
        x *= i

print(n - len(a))