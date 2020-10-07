Id, N, K = map(int, input().split())

listA=[] #appendのために宣言が必要
while True:
    try:
        listA.append(list(map(int,input().split())))

    except:
        break
        #または、quit(),os.exit()をして止める。

print(listA)
#[[1, 2, 2, 3, 1], [4, 5, 3, 4, 1, 2, 3, 4], [2, 3, 5, 6, 0, 2]]

if i = 0