AC = 0
WA = 0
TLE = 0
RE = 0

N = int(input())
for i in range(N):
    S = input()
    if S == 'AC':
        AC += 1
    if S == 'WA':
        WA += 1
    if S == 'TLE':
        TLE += 1
    if S == 'RE':
        RE += 1

print('AC'+' x '+{},AC)
print('WA'+' x '+{},WA)
print('TLE'+' x '+{},TLE)
print('RE'+' x '+{},RE)