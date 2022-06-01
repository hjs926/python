a,b=map(int,input().split())

def gcd(a,b): # gcd(b%a,a)
    return b if not a else gcd(b%a,a)

    print(gcd(a,b))