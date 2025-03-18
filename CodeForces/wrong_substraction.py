n, m = map(int, input().split())
for i in range(m):
    n = str(n)
    if n[-1] == '0':
        n = n[:-1]
    else:
        n = int(n)-1      
print(n)

   