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
    _min = min(_min, x)
    mcount = max(mcount, count[x])
avg = total / n
arr.sort()
mid = arr[n/2]
cnt = 0
mode = 0
for i in range(-4000, 4001):
    if mcount == count[i]:
        mode = 1
        cnt += 1
        if cnt == 2:
            break
rng = _max - _min
print(format(avg,'.0f'))
print(mid)
print(mode)
print(rng)
    