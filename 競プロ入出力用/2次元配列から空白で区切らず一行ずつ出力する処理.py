#2次元配列を空白で区切らず出力する
new_list = [[5,2,3,'y',0],['8','p','7',9],['6','m'],[3]]
for k in new_list:
    for j in k:
        print(j,end='')
    print()