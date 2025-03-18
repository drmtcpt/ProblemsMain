n, k = map(int, input().split())
a = 0
b = input().split()
for i in range(n):
    if int(b[i]) >= int(b[k-1]) and int(b[i]) > 0:
        a += 1
print(a)