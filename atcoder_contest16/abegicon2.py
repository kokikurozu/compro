X, Y = map(int, input().split())
if Y % 2 == 1:
    print("No")
elif (X * 2) <= Y <= (X * 4):
    print("Yes")
else:
    print("No")