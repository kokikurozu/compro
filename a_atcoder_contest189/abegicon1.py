c = list(str(input()))
x = c[1]
Is_flg = 1
for i in c:
    if x != i:
        print('Lost')
        Is_flg = 0
        break
if Is_flg == 1:
    print('Won')