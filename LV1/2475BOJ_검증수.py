# (백준 2475번, Class 1) 검증수
# for 문을 이용하여 계산할 것
arr = list(map(int, input().split()))
r = 0
for i in arr:
    r += i**2
print(r%10)
# 배열을 받고 list(map(int, input().split())) for문을 사용하여
# arr(어레이)에 있는 값을 하나씩 I에 들어가고 그 I를 제곱해서 r에 더해주고

# 리스트 컴프리헨션: 리스트를 만들 때 짧은 코드로 아주 용한 파이썬 문법
# [i for i in range(10)] - range(10)은 0부터 9까지 리스트를 만들어주고 하나씩 i를 가지고 오면 전체 리스트는 0부터 9까지 리스트가 된다

# [i**2 for i in range(10)] - 0부터 9까지 한개씩 가지고 오고 각각의 값을 제곱해준다

# [i**2 for i in map(int, input().split())]
# 입력받은것을 스플릿해서 인트로 모두 바꾼 map 객체를 한개씩 i로 가져오고 각각의 값을 제곱해준걸 가져온다.

# 짧은 방식 print(sum([i**2 for i in map(int, input().split())])%10)