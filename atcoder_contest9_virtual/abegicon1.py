Y, M ,T = input().split("/")
Y = int(Y)
M = int(M)
if Y < 2019:
    print("Heisei")
elif Y > 2019:
    print("TBD")
else:
    if M <= 4:
        print("Heisei")
    else:
        print("TBD")