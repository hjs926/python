from math import factorial

n, k = list(map(int,input().split()))

print(factorial(n)//(factorial(k)*factorial(n-k)))

# 다이나믹 프로그래밍 구현
# nCk = n-1Ck + n-1Ck-1