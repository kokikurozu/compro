X, Y, A, B = map(int,input().split())
keikenti = 0
while X < Y:
    if (X * A - X) <= B and X * A < Y:
        X = X * A
        keikenti += 1
    else:
        break

useB = (Y - 1 - X) // B
keikenti += useB
print(keikenti)