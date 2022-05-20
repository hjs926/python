# (백준 1000번, Class 1) A+B
# 1. map과 input, split을 사용하여 입력을 잘 받을 것
# 2. sum 또는 +를 이용하여 두 수를 합한 뒤 출력 할 것
a = list(map(int, input().split()))
print(a[0]+a[1])

# a라는 배열에 입력을 받을 때 input을 받고 split해주고 
# map함수를 이용해서 첫 번째는 int 두 번째 split된 리스트를 입력해주면 
# 안에 있는 모든 string 들이 int로 바뀌어서 map객체로 반환이 되게되는걸 리스트 형태로 바꾸어줌