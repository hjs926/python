# 1. arr[i+1] - arr[i]와 arr[i] - arr[i-1]의 곱을 구함
# 2. 0보다 크다면 같은 방향으로 증/감, 0보다 작다면 다른 방향이니 mixed
# 3. 반복문이 정상으로 돌았다면 arr[i] - arr[i-1]의 부호에 맞추어 asc, desc출력

arr = list(map(int, input().split()))
x = arr[1] - arr[0]
for i in range(1,7):
    y = arr[i+1] - arr[i]
    if x*y <= 0:
        print('mixed')
        break
    x = y
else:
    print('ascending' if x>0 else 'descending')
    