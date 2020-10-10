N = int(input())


if N % 2 == 0 and N != 2:
    print(int(N/2))
    for i in range(1, int(N/2), 1):
        print(2, i, 2 * N - i)

elif N % 2 == 1:

else:
    print('impossible')
    
    
    
    1 3 5 7 9 11 13 15 17 19 21 23 25 27 29

    225 = 5 5 3 3