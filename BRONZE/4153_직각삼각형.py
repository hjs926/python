# 배열.sort(): 배열이 오름차순으로 정렬됨
# sorted(배열): 오름차순으로 정렬된 배열을 반환함

while True:
    a,b,c = sorted(list(map(int, input().split())))
    if not a:
        break
    print('right' if c**2 == a**2 + b**2 else 'wrong')