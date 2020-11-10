N = list(input())
x = [0 for _ in range(len(N))]
have = [0,0,0]
for i in range(len(N)):
    x[i] = int(int(N[i]) % 3)
    have[x[i]] += 1

amari = sum(x) % 3

if amari == 0:
    print(0)
elif amari == 1:
    if have[1] >= 1:
        if sum(have) >= 2:
            print(1)
        elif sum(have) <= 1:
            print(-1)
    elif have[2] >= 2:
        if sum(have) >= 3:
            print(2)
        elif sum(have) <= 2:
            print(-1)
elif amari == 2:
    if have[2] >= 1:
        if sum(have) >=2:
            print(1)
        elif sum(have) <=1:
            print(-1)
    elif have[1] >= 2:
        if sum(have) >= 3:
            print(2)
        elif sum(have) <= 2:
            print(-1)
    else:
        print(-1)