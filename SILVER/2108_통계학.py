n = int(input())
arr = []
total = 0
count =[0]*(8001)
mcount = 0
_max = -40001
_min = 400001
for _ in range(n):
    x = int(input())
    arr.append(x)
    count[x] +=1
    total +=x
    _max = max(_max, x)
    _min = min(_minx, x)
    mcount = max(mcount, count[x])