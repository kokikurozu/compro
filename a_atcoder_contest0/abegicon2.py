N = int(input())
xi = list(map(int,input().split()))

man = 0
yu = 0
tyebi = 0
for i in xi:
    man += abs(i)
    yu += i**2

tyebi = max(max(xi), abs(min(xi)))

print(man)
print(yu ** 0.5)
print(tyebi)