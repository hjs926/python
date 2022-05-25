# n이 크지 않기 때문에 완전 탐색(모든 경우를 다 확인)
# 3중 반복문을 이용해 n장의 카드에서 3장을 뽑는 경우를 모두 확인
# 라이브러리 itertools

# from itertools import *
# print(*combinations(arr,2)) # (1,2) (1,3) (2,3)
n, m = map(int, input().split())
arr = list(map(int,input().split()))
result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[i] + arr[j] + arr[k] > m:
                continue
            else:
                result = max(result, arr[i]+arr[j]+arr[k])
print(result)