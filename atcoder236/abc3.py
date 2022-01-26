n,m = map(int,input().split())

s = list(map(str,input().split()))
t = list(map(str,input().split()))
j = 0

for i in t:
    while True:
        if i == s[j]:
            print('Yes')
            j += 1
            break
        else:
            print('No')
            j += 1