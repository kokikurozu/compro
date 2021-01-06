S = list(str(input()))
now_num = ''
Is = 1
for i in S:
    if i == now_num:
        Is = 0
        break
    else:
        now_num = i
if Is == 1:
    print('Good')
else:
    print('Bad')