T = int(input())
for i in range(T):
    N, A, B, C, D = map(int, input().split())
    a = 0
    b = 0
    c = 0
    d = 0
    coinNeed = 0
    coinNeed1 = D *N
    coinNeed2 = D
    coinNeed3 = D
    coinNeed5 = D
    NowNumber2 = 1
    NowNumber3 = 1
    NowNumber5 = 1
    while NowNumber2 * 2 < T:
        NowNumber2 *= 2
        coinNeed2 += A
    use2coinA = (T - NowNumber2) * D + coinNeed
    use2coinB = (NowNumber2 - T) * D + coinNeed
    coin2 = min(use2coinA, use2coinB)

    while NowNumber3 * 3 < T:
        NowNumber *= 3
        coinNeed3 += A
    use2coinA = (T - NowNumber) * D + coinNeed
    use2coinB = (NowNumber - T) * D + coinNeed
    coin3 = min(use2coinA, use2coinB)
