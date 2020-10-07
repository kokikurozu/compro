N = int(input())
maxX = 0
minX = 0
maxY = 0
minY = 0

while True:
    try:
        listA=list(map(int,input().split()))
        maxX = max(maxX, listA[0])
        minX = min(minX, listA[1])
        maxY = max(maxY, listA[0])
        minY = min(minY, listA[1])
    except:
        break
        #または、quit(),os.exit()をして止める。

print((maxX-minX) + (maxY-minY))