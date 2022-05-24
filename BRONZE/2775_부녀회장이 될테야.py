t = int(input())

dp = [[0]*15 for _ in range(15)]
dp[0] = [x for x in range(15)]

for i in range(1, 15):
    for j in range(1,15):
         dp[i][j] = dp[i][j-1] + dp[i-1][j]


for _ in range(t):
    k,n = int(input()), int(input())
    print(dp[k][n])


# 시간 복잡도
# 1. 단순 반복문을 이용했을 때:
#   각 호의 인원을 구할 때 최대 n번 반복
#   호가 대략 n2개 있으므로 시간 복잡도는 o(n3)
# 2. 다이나믹 프로그래밍을 이용했을 때:
#   각 호의 인원을 구할 떄 1번의 연산으로 구함
#   따라서 시간 복잡도는 o(n2)