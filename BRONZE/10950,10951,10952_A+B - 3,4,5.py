# 10950 A+B - 3
t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    print(a+b)

# 10951 예외처리구문 
# try:
#    a = int(input()) # input() = 'x' 인경우 자료형이 맞지 않는 경우 ValueError
#    print(a) # Error가 발생한 경우 a를 출력하지 않고 바로 except 구문으로 넘어감
# except:
#    print(1) # Error가 발생했으므로 1이 출력됨

# try 뒤에는 에러가 발생 될 거같은 코드를 적고  발생된다면 
# 그 뒤쪽 코드는 실행하지 않고 except문을 실행한다.
while True:
    try: 
        a,b = map(int,input().split())
        print(a+b)
    except:
        break

# 10952 
while True:
    a,b = map(int,input().split())
    if a==b==0:
        break
    print(a+b)