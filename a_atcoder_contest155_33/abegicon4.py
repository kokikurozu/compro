def cmb(n, r, mod):
    bunbo = 1
    bunshi = 1
    r = min(r, n - r)
    for i in range(r):
        bunshi = (bunshi * (n - i)) % mod
        bunbo = (bunbo * pow(i+1,mod-2,mod)) % mod
    return (bunbo * bunshi) % mod

mod = 10 ** 9 + 7
n, a, b = map(int,input().split())
ans = pow(2,n,mod) - 1
j = cmb(n, a, mod)
k = cmb(n, b, mod)
ans -= cmb(n, a, mod)
ans -= cmb(n, b, mod)
print(ans%mod)