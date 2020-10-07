X, K, D = map(int, input().split())
count = abs(int(X / D))#移動回数内で中央をまたげるか
if D > abs(X):
    if K % 2 == 1:
        last_place = abs(abs(X) - D)#Kが奇数の場合(済)
    else:
        last_place = abs(X)#(済)
else:
    if count <= K:#移動回数内で中央をまたげる場合
        if (K - count) % 2 == 1:#移動後残り移動回数が奇数の場合(済)
            last_place = abs(abs(X) - (count + 1) * D)
        else:
            last_place = abs(abs(X) - count * D)#(済)
    else:#(済)
        last_place = abs(abs(X) - D * K)
print(last_place)