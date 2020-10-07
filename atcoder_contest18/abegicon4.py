N, M = map(int, input().split())
listA=[]
count = 1
while True:
    try:
        now_list = list.sort((map(int,input().split())))
        if not (now_list in listA):
            listA.append(now_list)
    except:
        break
print(count)