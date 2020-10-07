N, M = map(int, input().split())
Ai = list(map(int, input().split()))

syukudai = sum(Ai)
nokori = N - syukudai
if nokori >= 0:
    print(nokori)
else:
    print(-1)