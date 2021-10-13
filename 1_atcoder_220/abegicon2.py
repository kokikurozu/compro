k = int(input())
a,b = map(str,input().split())
a = ''.join(reversed(a))
b = ''.join(reversed(b))
def change(x):
    ans = 0
    for i in range(len(x)):
        ans += (int(x[i]) * k ** i)
    return ans

A = change(a)
B = change(b)
print(A*B)