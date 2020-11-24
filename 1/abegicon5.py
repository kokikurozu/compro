N,A,B = map(int,input())
list_s = [0 for _ in range(N)]
for i in range(N):
    list_s[i] = int(input())

list_s.sort()

new_min = list_s[0]/A
new_max =