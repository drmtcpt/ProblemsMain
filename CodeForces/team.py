n = int(input())
arr = []
implement = 0
for i in range(n):
    a = str(input())
    arr.append(a)

for i in arr:
    if i.count('1') >= 2:
        implement += 1
        print(f'implement a problem {arr.index(i) + 1}')
    else:
        print(f"Don't implement {arr.index(i) + 1}")
        
if implement == 1:
    print(f'{implement} problem implemented')
else:
    print(f'{implement} problems implemented')