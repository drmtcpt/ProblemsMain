n = int(input())
a = []
k = 0
for i in range(n):
    operation = input()
    a.append(operation)
for _ in a:
    if _ == 'X++' or _ == '++X':
        k += 1
    elif _ == 'X--' or _ == '--X':
        k -= 1
    else:
        print(f'Invalid operation: "{_}"')
print(k)