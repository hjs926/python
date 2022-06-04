import sys
n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
for i in sorted(l):
    sys.stdout.write(str(i)+'\n')
# 1.  파이썬 -> 인터프리터 언어 느림
# 1-> pypy3 이용 = 파이썬, 데이터 처리 속도 향상, 메모리 많이
# 입출력 -> 표준 입출력
# 3.3 퀵 정렬 -> 최악의 경우 0(n^2)

# 1 2 3 4 5 6 7 8 9 10 -> 시간초과 x 메모리초과
# -> 피벗을 랜덤