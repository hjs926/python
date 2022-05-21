t = int(input())
for i in range(t):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)


t = int(input())
for _ in range(t):
    a,b = input().split()
    a = int(a)
    s = ''
    for x in b:
        s += x*a
    print(s)