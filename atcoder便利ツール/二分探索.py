#bisectの基本的な動作
#第一引数にリストを渡し、そのリストのどこに第二引数の値が
#挿入されるかを返す
#リスト内に同じ値があるなら、右に挿入するか左に挿入するかを
#bisect_right,bisect_leftで選択する

from bisect import *

l = [1,3,4,8,9,10,10,12]
print(bisect_right(l,13))