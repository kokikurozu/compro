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

N,M = map(int,input().split())
ai = list(map(int,input().split()))
bi = list(map(int,input().split()))
#cd = [list(map(int,input().split()))for _ in range(M)]

uf = UnionFind(N)
for i in range(M):
    c,d = map(int,input().split())
    uf.union(c-1,d-1)

a = uf.find(0)
IS_iudge = 1

ai_box = [0] * N
bi_box = [0] * N
for key in range(N):
    ai_box[uf.find(key)] += ai[key]
    bi_box[uf.find(key)] += bi[key]

if ai_box == bi_box:
    print('Yes')
else:
    print('No')