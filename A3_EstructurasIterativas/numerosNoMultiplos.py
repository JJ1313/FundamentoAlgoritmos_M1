n = int(input())
i = 1
while i <= n:
    if i % 3 != 0 and i % 7 != 0:
        print(i, end=" ")
    i += 1
