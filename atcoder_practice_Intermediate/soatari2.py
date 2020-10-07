A,B,K = map(int,input().split())
li = []
for i in range(1, min(A, B) + 1, 1):
    if A % i == 0 and B % i == 0:
        li.append(i)
print(li[-K])