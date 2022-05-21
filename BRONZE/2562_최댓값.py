_max = 0
idx = -1 
for i in range(1,10):
    a = int(input())
    if a>_max:
        _max = a
        idx = i
print(_max)
print(idx)

# max값과 그 변수가 몇번째인지 아는 index 값을 지정한다
# 하나씩 받으면서 내가저장한 max값보다 받은 값이 크면 값을 저장하고
# 이값의 index도 저장해서 최종적으로 가장 큰 값이 남고 index 값이 남도록 한다.

arr=[]
for i in range(9):
    arr.append(int(input()))
    
print(max(arr))
print(arr.index(max(arr))+1)
# arr라는 리스트 생성 
# for 반복문을 사용하여 9번 반복 이떄 입력값을 받게 되는데 
# 정수형으로 입력받고 append에 의해 arr라는 리스트에 하나씩 추가됨
# arr리스트의 최대값 출력
# arr 최댓값의 index(위치) 반환, 이때 index의 위치는 0부터 시작하므로 +1을 해준다

