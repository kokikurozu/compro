import collections
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

A,B = map(int,input().split())
list_A = collections.Counter(prime_factorize(A))
list_B = collections.Counter(prime_factorize(B))
new_dict = {}
a = list(list_A.keys())
b = list(list_B.keys())

new_set = set(a + b)
for i in new_set:
    x = 0
    y = 0
    if i in list_A:
        x = list_A[i]
    if i in list_B:
        y = list_B[i]
    new_dict[i] = max(x, y)
cnt = 1
for key in new_dict.keys():
    cnt = cnt * key ** new_dict[key]
print(cnt)