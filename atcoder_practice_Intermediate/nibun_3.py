def binary_search(listAA, target):
    low = 0
    high = len(listAA) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = listAA[mid]
        if guess == target:
            return 1
        if guess >= target:
            high = mid - 1
        else:
            low = mid + 1
    return 0

n = int(input())
listA = list(map(int, input().split()))
q = int(input())
listB = list(map(int, input().split()))
cnt = 0

for now_target in listB:
    cnt += binary_search(listA, now_target)

print(cnt)