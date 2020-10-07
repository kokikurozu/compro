T = ''
S = str(input())
a = 'dream'
b = 'dreamer'
c = 'erase'
d = 'eraser'

S = S.replace('dreamer', ' ')
S = S.replace('eraser', ' ')
S = S.replace('dream', '')
S = S.replace('erase', '')
S = S.strip(' ')
print(S)
if S == '':
    print('Yes')
else:
    print('NO')