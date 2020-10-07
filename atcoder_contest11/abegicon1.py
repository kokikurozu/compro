S = list(input())
T = list(input())
S.append(T[len(T) - 1])
if S == T:
    print("Yes")
else:
    print("No")

