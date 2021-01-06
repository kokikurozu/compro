n,l = map(int,input().split())
list_apple = [l+i for i in range(n)]
if list_apple[n-1] >= 0 and list_apple[0] >= 0:
    x = list_apple[0]
elif list_apple[0] <= 0 and list_apple[n-1] <= 0:
    x = list_apple[n-1]
else:
    x = 0

print(sum(list_apple) - x)