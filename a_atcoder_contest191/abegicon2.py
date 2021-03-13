n,x = map(int,input().split())
ai = list(map(int,input().split()))
new_ai = [s for s in ai if s != x]
print(*new_ai)