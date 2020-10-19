A,B,C = map(int,input().split())

if (A == B and A != C) or (B == C and C != A) or (A == C and B !=C ):
    print('Yes')
else:
    print('No')