n = list(input())
n_start = 0
n_fin = 0
for i in range(len(n)):
    if n[i] == '0':
        n_start += 1
    else:
        break
for j in range(len(n)-1,-1,-1):
    if n[j] == '0':
        n_fin += 1
    else:
        break
n.reverse()
if n_start < n_fin:
    for j in range(n_fin-n_start):
        n.append('0')
    
if n == n[::-1]:
    print('Yes')
else:
    print('No')