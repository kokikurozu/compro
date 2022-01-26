l,r = map(int,input().split())
s = str(input())
rx = s[::-1]
new_x = s[:l-1] + rx[len(s)-r:len(s)-l+1] + s[r:]
print(new_x)