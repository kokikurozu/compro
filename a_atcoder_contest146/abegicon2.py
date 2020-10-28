N = int(input())
S = str(input())

a = S[0:len(S)//2]
b = S[len(S)//2::]
if a == b:
    print('Yes')
else:
    print('No')