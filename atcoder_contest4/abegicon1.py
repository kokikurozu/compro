N = list(input())
judge = False
for i in N:
    if int(i) == 7:
        judge = True
if judge == True:
    print("Yes")
else:
    print("No")