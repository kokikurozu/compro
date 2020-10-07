N = int(input())
name = []
S = ''
num = 26
for i in range(20):
    amari = int(N % num)
    if amari == 0:
        amari = 112
    else:
        amari += 96
    N = int(N / num)
    amari = chr(amari)    
    name.insert(0, amari)
    if N / num == 0:
        break

for l in name:
    S = S + l
print(str(S))
