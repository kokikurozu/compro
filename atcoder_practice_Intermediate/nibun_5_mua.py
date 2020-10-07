def nibun_search(listAA, target):#目的の数値の場所を返す関数
    low = 0
    high = len(listAA) - 1
    while low <= high:
        mid = (low + high) // 2#//は小数点以下は切り捨てられる演算子
        now_list = listAA[mid]
        if now_list == target:
            return mid
        elif now_list > target:
            high = mid - 1
        else:
            low = mid + 1
    return 0

P = float(input())