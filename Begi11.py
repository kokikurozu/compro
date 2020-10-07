import math
A, B = map(int, input().split())
taxA = A / 8 * 100
taxB = B * 10
judge = True
litaxB = [taxB + i for i in range(10)]
if taxA - int(taxA) < 0.5:
    litaxA = [int(taxA) + j for j in range(13)]
else:
    litaxA = [int(taxA) + 1 + j for j in range(12)]
for k in litaxA:
    if k in litaxB:
        print(k)
        judge = False
        break
if judge == True:
    print(-1)