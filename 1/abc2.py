n = int(input())
x = [input() for i in range(n)]
koho = list(set(x))
koho_cnt = [0 for i in range(len(koho))]
for i in range(len(koho)):
    koho_cnt[i] = x.count(koho[i])
print(koho[koho_cnt.index(max(koho_cnt))])