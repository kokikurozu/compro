t = int(input())
mod = 10**9 + 7
for i in range(t):
    N,Ag,Bg,Ac,Bc,Ap,Bp = map(int,input().split())

    p1 = pow( Ag*pow(Bg,mod-2,mod) + Ac*pow(Bc,mod-2,mod), N, mod )#分数の合同式は分子前に、分母を第一引数になる
    p2 = pow( Ac*pow(Bc,mod-2,mod) + Ap*pow(Bp,mod-2,mod), N, mod )
    p3 = pow( Ap*pow(Bp,mod-2,mod) + Ag*pow(Bg,mod-2,mod), N, mod )
    
    p4 = pow( Ag*pow(Bg,mod-2,mod), N, mod )
    p5 = pow( Ac*pow(Bc,mod-2,mod), N, mod )
    p6 = pow( Ap*pow(Bp,mod-2,mod), N, mod )

    ans = 1 - (p1+p2+p3) + 2*(p4+p5+p6)
    print(ans%mod)

