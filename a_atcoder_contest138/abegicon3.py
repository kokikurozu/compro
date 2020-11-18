N = int(input())
list_S = [0 for i in range(N)]
for i in range(N):
    s = list(input())
    s.sort()
    list_S[i] = s

list_S.sort()
now_word = ''
cnt = 0
ans = 0

for i in list_S:
    if i == now_word:
        ans += cnt
        cnt += 1
    else:
        ans += cnt
        cnt = 0
        now_word = i

ans += cnt
print(ans)