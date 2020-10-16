N, M = map(int,input().split())
sc=[list(map(str,input().split()))for _ in range(M)]

if N == 1:
    number = ['0']
else:
    number = ['1']
    for i in range(N-1):
        number.append('0')


for s,c in sc:
    number[int(s)-1] = c

for s1,c1 in sc:
    for s2,c2 in sc:
        if s1 == s2 and c1 != c2:
            number = '-1'
            break

if len(number) != 1 and number[0] == '0':
    number = '-1'

print(int(''.join(number)))