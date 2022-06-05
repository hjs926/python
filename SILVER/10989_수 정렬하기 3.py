n = int(input())

sortList = [0]*10001

for i in range(n):
    sortList[int(input())] += 1

for i in range(1, 10001):
    for j in range(sortList[i]):
        print(i)