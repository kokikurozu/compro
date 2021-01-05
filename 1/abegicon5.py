T = int(input())
for i in range(T):
    n,s,k = map(int,input().split())
    ans = 0 # 移動回数の記録
    cnt = 1
    now = s #現在位置の記録
    mod = n
    #初期位置探し
    if n < k:
        k = k % n
    z = (n - s) // k
    ans += z
    now += z * k
    if now == n:
        ans = - 1
    else:
        ans += 1
        now = (now + k) % n #玉座から一回時計回りの位置に行く処理
    if n / 2 < k: #椅子の数の半分以上進んでしまう場合
        k = (2 * k) % n
        cnt *= 2
    while ans:
        z = (n-now) // z * k
        now += z * k
        ans += cnt
        if now == n:
            break
        else:
            now = (now + k) % n
    print(ans)