# join함수, 리스트 컴프리헨션
# print(''.join(['p','y','t','h','o','n'])) 출력 python
# print(' '.join(map(str, [1,2,3,4,5]))) 출력 1 2 3 4 5
# print

n,x = map(int,input().split())
a = list(map(int,input().split()))
print(' '.join(map(str,[i for i in a if i<x])))