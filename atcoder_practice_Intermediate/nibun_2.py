def nibun_search(listA, target):#目的の数値の場所を返す関数
    low = 0
    high = len(listA) - 1
    listA.sort()
    print(listA)
    while low <= high:
        mid = (low + high) // 2#//は小数点以下は切り捨てられる演算子
        now_list = listA[mid]
        if now_list == target:
            return mid
        elif now_list > target:
            high = mid - 1
        else:
            low = mid + 1
    return "ありません"

my_list = [1, 3, 5, 7, 9]
print(nibun_search(my_list, 3))
print(nibun_search(my_list, -1))



