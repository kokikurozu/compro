N = list(str(input()))
K = int((input()))

for i in range(len(N) - 1):
    if ord(N[i]) >= 98 and K >= 123 - int(ord(N[i])):
        K = K - (123 - ord(N[i]))
        N[i] = 'a'
a = ord(N[len(N)-1]) + K
if a > 122:
    b = (a - 98) % 25
    a = b + 97
N[len(N)-1] = chr(a)
"""for j in N:
    print(j, end='')"""
print(','.join(N))