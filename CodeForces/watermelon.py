weight = int(input())

for i in range(weight):
    a = weight - i
    if a%2==0 and i%2==0:
        print('YES')
        break
    else:
        print('NO')
        break
    