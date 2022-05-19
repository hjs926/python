# (백준 2438, 2439번, Class 1) 별찍기
n = int(input())
for i in range(1,n+1):
    print('*'*i)

# i를 1부터 n까지 받고 출력할때 공백을 n-i개 하고 *를 i개만큼 곱해준다.
n = int(input())
for i in range(1,n+1):
    print(' '*(n-i)+'*'*i)
