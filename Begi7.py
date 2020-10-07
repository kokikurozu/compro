N = list(input())
m = 0
cnt = 0
for x in N:
    
    if x == 'A' or x == 'C' or x == 'G' or x == 'T':
        cnt += 1
    else:
        m = max(cnt, m)
        cnt = 0

m = max(cnt, m)

print(m)