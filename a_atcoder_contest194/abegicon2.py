a,b,w = map(int,input().split())
w = w*1000
a_judge = 0
b_judge = 0
is_flg = 0
for i in range(1000000):
    a_judge += a
    b_judge += b
    if a_judge <= w <= b_judge:
        is_flg = 1
if is_flg == 0:
    print('UNSATISFIABLE')
else:
    x = w//b
    if w//b == 0:
        x = 1    
    print(-(-w//b),end = ' ')
    print(w//a)