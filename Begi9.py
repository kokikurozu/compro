N, A, B = map(int, input().split())
roop = int(N / (A + B))
nokori = N - roop * (A + B)
if nokori == 0:
    ans = roop * A
elif nokori <= A:
    ans = roop * A + nokori
else:
    ans = roop * A + A
print(ans)