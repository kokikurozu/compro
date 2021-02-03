#勝率0.45で1000戦やったらマスターになれるか
from random import random
now_rank = 1
now_rensyo = 0
print('勝率を入力して下さい(小数)')
win_rate = float(input())
get_mas = 0
pla = 0
for j in range(10000):
    for i in range(100):
        x = random()
        if x <= win_rate:
            now_rensyo += 1
            if now_rensyo <= 2:
                now_rank += 1
            else:
                now_rank += 2
        else:
            if now_rank >= 2:
                now_rank -= 1
                now_rensyo = 0
        if now_rank >=26:
            #print('マスターを達成しました')
            get_mas += 1
            now_rank = 1
            now_rensyo = 0
            break
    now_rank = 1
    now_rensyo = 0
get_mas = str(get_mas)
pla = str(pla)
print('マスター達成数は' + get_mas + 'です')
print('マスター未達成数は' + pla + 'です')