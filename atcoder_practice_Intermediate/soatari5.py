N = int(input())
S = str(input())

numbers = set()

for i in range(0, len(S), 1):
    for j in range(i+1, len(S), 1):
        for k in range(j+1, len(S), 1):
            number = (S[i],S[j],S[k])
            numbers.add(number)
print(len(numbers))


"""for x in range(10):
    for y in range(10):
        for z in range(10):
            lucky_number = [str(x), str(y), str(z)]
            if lucky_number in numbers:
                cnt += 1

print(cnt)"""