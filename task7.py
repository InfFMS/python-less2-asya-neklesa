n = int(input())
for i in range(2, n+1):
    dog = 0
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            dog += 1
    if dog == 0:
        print(i)
