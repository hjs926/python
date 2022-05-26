# # 초기화 i=0; j=lenght-1
# def palidrome(s):
#     i,j = 0, len(s)-1
#     while i<j:
#         if s[i] == s[j]:
#             i+=1
#             j-=1
#         else:
#             return 'no'
#     return 'yes'

# while True:
#     s = input()
#     if s == '0':
#         break
#     print(palidrome(s))

def palindrome(s):
    return s == s[::-1]

while True:
    s = input()
    if s == '0':
        break
    print('yes' if palindrome(s) else 'no')