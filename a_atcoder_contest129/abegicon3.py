n = int(input())
string_list=[input()[::-1] for i in range(n)]
string_list.sort()
Is_flg = 0
for i in string_list:
    if i[-1] != '!':
        n = i + '!'
    else:
        if n == i:
            print(n[::-1].lstrip('!'))
            Is_flg = 1
            break

if Is_flg == 0:
    print('satisfiable')
