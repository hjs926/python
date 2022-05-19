# format함수 사용
# format 함수: 문자열 안에 중괄호가 있을때 중괄호를 인식해서 안에다가 원하는 값을 넣어준다.

n = int(input())

for i in range(1,10):
    print('{} * {} = {}'.format(n,i,n*i))