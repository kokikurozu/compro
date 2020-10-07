N=int(input())
lst=[[] for _ in range(N)]
for i in range(N):
  for j in range(int(input())):
    x,y=map(int,input().split())
    x-=1
    lst[i].append([x,y])
ans=0
for i in range(2**N):
  honest=[]
  unkind=[]
  flag=0
  for j in range(N):
    if (i>>j)&1:        # jは正直者
      honest.append(j)
    else:
      unkind.append(j)
  for p in honest:
    for l in lst[p]:
      x,y=l[0],l[1]
      if y:
        if x in unkind:
          flag=1
          break
      else:
        if x in honest:
          flag=1
          break
  if flag!=1:
    ans=max(ans,len(honest))
print(ans)