
arr = [int(input())for _ in range(n)]

def qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr.pop()
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]

    return qsort(left) + [pivot] + qsort(right)

    for x in qsort(arr):
        print(x)

