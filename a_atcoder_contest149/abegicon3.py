def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

X = int(input())

while True:
    target = prime_factorize(X)
    if len(target) == 1:
        break
    X += 1
print(target[0])