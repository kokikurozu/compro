N = int(input())
S = []
for i in range(N):
    S.append(input())

S.sort()
S.append('')

now_word = ''
now_max = 0
cnt = 0
word_list = []

for i in S:
    if now_word == i:
        cnt += 1
    else:
        if cnt > now_max:
            now_max = cnt
            word_list = []
            word_list.append(now_word)
        elif cnt == now_max:
            word_list.append(now_word)
        cnt = 1
        now_word = i

for i in word_list:
    print(i)