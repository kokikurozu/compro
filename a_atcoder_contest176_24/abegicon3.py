N = int(input())
Ai = list(map(int,input().split()))
humidai = 0
now_top = 0
for i in Ai:
    if now_top <= i:
        now_top = i
    humidai += now_top - i
print(humidai)