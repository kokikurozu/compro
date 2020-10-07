def nibun_search(listAA, target):#目的の数値の場所を返す関数
    low = 0
    high = len(listAA) - 1
    while low <= high:
        mid = (low + high) // 2#//は小数点以下は切り捨てられる演算子
        now_list = listAA[mid]
        if now_list == target:
            return mid - 1
        if low == high:
            return mid
        elif now_list > target:
            high = mid - 1
        else:
            low = mid + 1
    return 0

N = int(input())
listA = list(map(int, input().split()))
listB = list(map(int, input().split()))
listC = list(map(int, input().split()))
listA.sort()
listB.sort()
listC.sort()
count = 0

for C in listC:
    use_B = nibun_search(listB, C)
    i = 0
    for B in listB:      
        use_A = nibun_search(listA, B)
        if B > listA[use_A]:
            count += 1
        if i == use_B:
            break
        i += 1
        count += use_A

print(count)