def point(x,r):#xは手札の配列 rは現在引いた#のカード
    points = 0
    x[4] = r
    for t in range(1,10,1):
        points += t * 10 ** x.count(t)
    return points

from copy import deepcopy
k = int(input())
s = list(input())
for i in range(4):
    s[i]=int(s[i])
t = list(input())
for i in range(4):
    t[i]=int(t[i])
ai = [0] + list(k for i in range(9))

for i in range(4):
    ai[int(s[i])] -= 1
for i in range(4):
    ai[int(t[i])] -= 1
rem_cards = 9*k-4

#ai_ori = deepcopy(ai)
win_s = 0
win_t = 0

for i in range(1,10,1):
    ai_ori = deepcopy(ai)# #のカードを元の状態にする
    point_s = point(s,i) # #に引いたカードを割り当て、得点を計算
    count_card = ai_ori[i]
    ai_ori[i] -= 1 # 引いたカード分を減らす
    for j in range(1,10,1):
        point_t = point(t,j)
        if point_s > point_t:
            win_s += count_card * ai_ori[j]
        else:
            win_t += count_card * ai_ori[j]

print(win_s/(win_t + win_s))