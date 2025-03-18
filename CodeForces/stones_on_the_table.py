n = int(input())
stonesColour = str(input())
rc = 0

if n == len(stonesColour):
    for i in range(1, n):
        if stonesColour[i] == stonesColour[i - 1]:
            rc += 1
print(rc)

