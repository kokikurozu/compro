N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
L = [1] * N # 判定用

i = 0
koma = i
score = 0

now_list = []
all_list = []

for j in L:
    if j == 1:
        while True:
            now_i = i
            now_i = P[now_i]
            now_list.append(C[now_i])
            L[now_i] = 0
    
            if koma == now_i:
                all_list.append(now_list)
                break
for k in all_list:
    if sum(k) <= 0:
        k <= 0
        now_max = sum(k) * (K / len(k))

print(now_max)