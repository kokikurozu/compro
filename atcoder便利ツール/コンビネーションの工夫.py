def cmb(N,R,M):
    C=[1]*(R+1)
    for i in range(1,R+1):
        C[i]=(C[i-1]*(N+1-i)*pow(i,M-2,M))%M
    return C

def cmb2(n, r, mod):
    bunbo = 1
    bunshi = 1
    r = min(r, n - r)
    for i in range(r):
        bunshi = (bunshi * (n - i)) % mod
        bunbo = (bunbo * pow(i+1,mod-2,mod)) % mod
    return (bunbo * bunshi) % mod