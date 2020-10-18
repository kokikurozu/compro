listA = [2,5,3,6,11]

def LIS(L):
  from bisect import bisect
  seq=[]
  for i in L:
    pos=bisect(seq,i)
    if abs(len(seq) - pos) >= 3:
      seq.append(i)
    else:
      seq[pos]=i
  return len(seq)

print(LIS(listA))