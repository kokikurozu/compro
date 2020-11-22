a, b = map(int,input().split())
c, d = map(int,input().split())

if a == c and b == d:
    print(0)#ただ座標が全く同じなら、という条件
elif a + b == c + d or a - b == c - d or abs(a-c) + abs(b-d) <= 3:
    print(1)#設問通りの条件
elif (a+b+c+d) % 2 == 0 or abs(c-a) + abs(d-b) <= 6 or abs(abs(c-a)-abs(d-b)) <= 3:#一応(c-a)+(d-b) % 2 == 0にしておく
    print(2)
else:
    print(3)#2回斜めで行ける範囲を思い浮かべれば3回で行けないはずはない
