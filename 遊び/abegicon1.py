from random import random
now_rank = 1
now_rensyo = 0
print('勝率を入力して下さい(小数)')
win_rate = float(input())
for i in range(1000):
    x = random()
    if x <= win_rate:
        now_rensyo += 1
        if now_rensyo <= 2:
            now_rank += 1
        else:
            now_rank += 2
    else:
        now_rank -= 1
        now_rensyo = 0
    if now_rank >=26:
        print('マスターを達成しました')
        break
if now_rank <= 25:
    print('マスター未達成です')