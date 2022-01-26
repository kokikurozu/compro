n,k = map(int,input().split())
ai = list(map(int,input().split()))
wa = ai[0]
l = 0
r = 0
ans = 0
while True:
    if wa == k:
        ans += 1
    if l == r and r < n:
        r += 1
        wa += ai[r]
    else:
        if wa == k and r < n:
            r += 1
            wa += ai[r]
        elif wa > k:
            if r < n:
                try:
                    if ai[r+1] <= 0:
                        r += 1
                        wa += ai[r]
                except:
                    pass
                        
                if ai[l] < 0:
                    l += 1
                    wa -= ai[l]

                
        if wa <= k:
            if ai[l] >= 0 and r < k:
                r += 1
                wa += ai[r]
            else:
                l += 1
                wa -= ai[l]

    if l == n:
        break