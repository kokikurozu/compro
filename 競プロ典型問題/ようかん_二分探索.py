n, l = map(int,input().split())
k = int(input())
ai = list(map(int,input().split()))
ai.append(l)
score_ai = [0] * (n+1)
score_ai[0] = ai[0]
for i in range(len(ai)-1):
    score_ai[i+1] = ai[i+1] - ai[i]

def is_ok(arg):
    is_flg = 1
    piece = 0
    cut = 0
    for i in range(n+1):
        if piece < arg:
            piece += score_ai[i]
        else:
            cut += 1
            piece = score_ai[i]
    if cut < k:
        is_flg = 0
    if piece < arg and cut == k:
        is_flg = 0

    return is_flg


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

print(meguru_bisect(l+1, 0))
