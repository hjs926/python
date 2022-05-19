# (백준 1330번, Class 1) 두 수 비교하기
a, b = map(int, input().split())
if a>b:
    print('>')
elif a<b:
    print('<')
else:
    print('==')
# 더보기(삼항연산자)A if 논리값 else B (a가 b보다 클때 a값을 출력하고 아니면 b출력)
# a, b = map(int, input().split())
# print('>' if a>b else('<' if a<b else '=='))