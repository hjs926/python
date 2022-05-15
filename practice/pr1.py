# 인덱싱 a="abcd e" a[2]=c a[5]=e 
# 슬라이싱 [이상:미만:간격] b[::-2] 뒤로두칸
#포멧팅
#a = "my age is {age}".format(age="27")
#print(a)

#b = "%.4f" % 3.141592
#print(b)

# 문자열 개수 세기(count) a="hobby" a.count('b) //2 
# 위치 알려주기 (find)  a="abcdefg"  a.find('b') //3 없으면 -1이 나옴

# 문자열 삽입
#a="," .join("abcd")
#print(a)

#소문자 대문자 바꾸기 upper lower  a.upper() a.lower()

# a.strip() 공백 제거

# replace 문자열 바꾸기

# apped 맨 뒤에 추가한다 insert(0,4) 0번째 인덱스에 4추가

# sort 가나다 알파벳 순 숫자순

# remove(1) 1이라는 값을 삭제

# pop() 리스트요소 끄집어 내기

# a.count(1) 1이 몇개 있는지 세준다

# a.extend([2,3]) 리스트 확장 (리스트에 추가해준다)

# 리스트와 튜플의 차이 리스트는 변경가능 튜플은 변경불가능

# 딕셔너리 자료형 
# a=1{1:'a'}
# a['name'] = "익명"
# 삭제 del a[1]
# print(a)   >>> 
# key가 중복되면 안된다.  딕셔너리는 키가 핵심

# a.keys()  a.values()  a.items()


# Q1 홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해 보자.


a = 80
b = 75
c = 55
d = 35
print((a+b+c)/3)