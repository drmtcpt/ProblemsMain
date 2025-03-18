n = int(input())
s = []

for i in range(n):
    word = input()
    if len(word) > 10:
        word = word[0] + str(len(word) - 2) + word[-1]
        s.append(word)
    else:
        s.append(word)
for i in s:
    print(i)