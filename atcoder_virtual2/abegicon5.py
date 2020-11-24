N,A,B = map(int,input().split())
list_s = [0 for _ in range(N)]
for i in range(N):
    list_s[i] = int(input())
P = 'x'
list_s.sort()
ave = sum(list_s)/len(list_s)
min_s = list_s[0]
max_s = list_s[len(list_s)-1]
try:
    P = 1/((max_s-min_s)/B)
    Q = A - ave*P
except:
    pass
if list_s[len(list_s)-1] < 0 or P == 'x':
    print(-1)
else:
    print(P,Q)