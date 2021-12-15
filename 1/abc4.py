class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):#対象の要素がどの箱に入っているか検索
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):#2つの箱を一緒の箱にする。箱の番号は前の番号に依存する
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):#箱の要素数を調べる
        return -self.parents[self.find(x)]

    def same(self, x, y):#同じ箱に入っているか調べる
        return self.find(x) == self.find(y)

    def members(self, x):#要素xが所属するグループ
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):#残っている箱を全て配列として表示
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):#箱の数を見ている
        return len(self.roots())

    def all_group_members(self):#全ての箱を辞書型でくれる
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
       return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())



n,m = map(int,input().split())
uf = UnionFind(n+1)
x = [0,0]
s = [[0,0]] + [list(map(int, input().split())) for _ in range(m)]
con = [[0,0] for i in range(n+1)]
judge = 'Yes'
for i in range(1,m+1):
    #循環の判定
    if uf.same(s[i][0],s[i][1]) == 1:
        judge = 'No'
        break
    uf.union(s[i][0],s[i][1])
    # [0]を判定
    if not(0 in con[s[i][0]]) and not(s[i][1] in con[s[i][0]]):
        judge = 'No'
        break
    # [1]を判定
    if not(0 in con[s[i][1]]) and not(s[i][0] in con[s[i][1]]):
        judge = 'No'
        break
    #判定に引っかからない時繋がりの入力をする
    v = con[s[i][0]].index(0)
    w = con[s[i][1]].index(0)

    con[s[i][0]][v] = s[i][1]
    con[s[i][1]][w] = s[i][0]



print(judge)