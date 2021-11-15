n = int(input())
s = [list(input().split()) for i in range(n)]
print(s)



#intで取れる
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
print(s)