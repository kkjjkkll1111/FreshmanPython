# 1. 타입변환
a = 10
b = float(a)
c = bool(a)
d = str(a)

#출력 해보기
# print(type(a), a)
# print(type(b), b)
# print(type(c), c)
# print(type(d), d)


# 2. 문자열 포멧팅
name = "홍길동"
age = 25

#다 한번씩 써보기
'''
#1번(자주 안씀)
print("내이름은 " + name + "입니다, 나이는 " + str(age) + "살입니다")
#2번(자주 안씀)
print("내이름은 %s입니다, 나이는 %s살입니다"%(name, age))
#3번(자주 안씀)
print("내이름은 {0}입니다, 나이는 {1}살입니다".format(name, age))
#4번(이걸 자주씀)
print(f"내이름은 {name}입니다, 나이는 {age}살입니다")
'''


# 3. 입력(input)

# a = input()
# print(a)

# 원하는 문장을 출력한다음 입력 받을 수 있음
# a = input("입력하세요\n")
# print(a)

# input으로 받은 값은 무조건 문자열(타입변환이 필수)
# x = input("숫자1 : ")   # 10
# y = input("숫자2 : ")   # 20
# print(x + y)           # 1020

# 방법1
# x = int(input("숫자1 : "))   # 10
# y = int(input("숫자2 : "))   # 20
# print(x + y)                # 30

# 방법2
# x = input("숫자1 : ")       # 20
# y = input("숫자2 : ")       # 20
# print(int(x) + int(y))     # 30


# 4. 문자열 슬라이싱
a = "hello"
# 방법
# a[시작값:끝값:증가값]

# 예상값 작성하고 출력해보기
# print(a)          # hello
# print(a[0])       # ???
# print(a[1:])      # ???
# print(a[1:4])     # ???
# print(a[::2])     # ???
# print(a[-1])      # ???
# print(a[::-1])    # ???


# 5. 문자열 메소드 (모두 출력해보기)
test = "do python for funny"

# 5-1. count(문자 세는 역할)
# print(test.count('o'))        # 3
# print(test.count('O'))        # ???

# 5-2. find(문자열이 어디에 있는지 확인, 인덱스 반환)
# print(test.find('o'))         # 2
# print(test.find('q'))         # ??
# print(test.find('on'))        # ??
# print(test.find('qn'))        # ??

# 5-3. index(문자열이 어디에 있는지 확인, 인덱스 반환)
# print(test.index('o'))        # 2
# print(test.index('q'))        # ???
# print(test.index('on'))       # ???

# 5-4. if문 조건 바꿔서 출력해보기
# if "qn" in test:
#     print(test.index('qn'))
# else:
#     print("없다")

'''
index vs find

find : 찾고자 하는 문자열이 없는 -1 리턴
index : 찾고자 하는 문자열이 없는 경우 에러발생
'''

# 5-5. 대소문자 관련 메소드
'''
# 대문자
print(test.upper())
# 소문자
print(test.lower())
# 단어 첫 스펠링 대문자
print(test.title())
# 문장 첫 스펠링 대문자
print(test.capitalize())
'''

# 5-6. join(문자 사이사이에 원하는 값 끼워넣기)
# print(" ".join(test))
# 예상 출력값 적어보기


# 5-7. strip(공백 제거, 방향 지정 가능)
test = "   Tralalero Tralala   "
# print("|" + test + "|")
# print("|" + test.strip() + "|")
# print("|" + test.lstrip() + "|")
# print("|" + test.rstrip() + "|")

# 5-8. replace (원하는 문자열을 다른 문자열로 치환해준다)
# print(test.replace("Tralala","mola")) #바뀐 다음 저장하고 저장된 위치를 다시 알려준다
# print(test) # 원래 위치

# 5-9. split(문자열 쪼개기, 기본값 : 스페이스)
# print(test.split())
# print(test.split("r")) # i기준으로 쪼개짐(단, 쪼개지는 기준은 삭제된다)



