# set() 명령어는 중복을 제거하는 역할을 한다
# set은 집합과 같다 [1, 1, 2, 3, 4, 4] -> {1, 2, 3, 4}
# set의 생성자를 통해 list를 set으로 바꾸어 줄수 있다.

arr = [int(input())%42 for _ in range(10)]
print(len(set(arr)))