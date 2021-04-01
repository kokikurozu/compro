kakko_list = []
N = int(input())
for i in range(2**N):
    ls = ['(']*N
    for j in range(len(ls)):
        if (i >> j) & 1:
            ls[j] = ')'
    cnt = 0
    cnt_0 = 0
    cnt_1 = 0
    is_flg = 1
    for j in range(len(ls)):
        if ls[j] == '(':
            cnt += 1
            cnt_0 += 1
        else:
            cnt -= 1
            cnt_1 += 1
        if cnt < 0:
            is_flg = 0
            break
    if cnt_0 != cnt_1:
        is_flg = 0
    if is_flg: 
        kakko_list.append(''.join(ls)) #この位置にbit列が用意されるので、ここにコードを書く
kakko_list.sort()
print(*kakko_list)

#N個のビット列がすべてlsに格納される
#appendを利用する場合
'''
N = 3
ls_list = []
for i in range(2**N):
    ls = [1]*N
    for j in range(len(ls)):
        if (i >> j) & 1:
            ls[j] = 0
    ls_list.append(ls)
print(ls_list)
'''