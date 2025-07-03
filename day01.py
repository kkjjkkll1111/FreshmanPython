# 1. 주석,
# 짧은 주석은 '#'을, 긴 주석은 """ """을 사용


# 2. 파이썬 VS C언어
"""
파이썬 VS C언어

C언어의 특징:
컴파일 언어
속도가 빠름
타입선언이 필요함
문법이 비교적으로 어려움

파이썬 특징:
인터프리터 언어
속도가 느림
타입선언이 필요없음
문법이 매우 쉬움


인터프리터 VS 컴파일러
프로그램 전체를 스캔하여 이를 모두 기계어로 번역한다 <= 컴파일러
프로그램 실행시 한 번에 한 문장씩 번역한다.  <= 인터프리터

장단점 :
인터프리터 : 메모리 사용량 ↑, 속도 ↓
컴파일러 : 메모리 사용량 ↓, 속도 ↑

"""


# 3. 변수 선언
a = 1.1
b = 10
c = "안녕하세요"
# print(a, b, c)     # 1.1 10 안녕하세요

# 3-1. 변수의 타입

#변수의 타입은 뒤에 있는 값에 따라 달라짐
a = 10
b = 3.14
c = "안녕하세요?"
# print(type(a))    #int
# print(type(b))    #float
# print(type(c))    #str

# 4. print
"""
print는 C언어의 printf와 비슷한 역할을 한다.
무언가를 출력할 때 사용하는 함수이며, 기본적으로 출력 후 줄바꿈을 수행한다.

sep : 여러 값을 출력할 때 값 사이에 넣을 구분자(기본값: ' ')
end : 출력이 끝난 뒤에 넣을 문자(기본값: '\n')

"""

a = 10
b = 20
# print("a")    # a
# print(a)      # 10
# print(a + b)  # 30
# print(a, b)   # 10 20

# 4-1. sep 활용(출력값 예상해서 ???에 맞는 값 적어 보기)
# print("I","Have","A","Pen")                   # I Have A Pen
# print("I","Have","A","Pen", sep="")           # IHaveAPen
# print("I","Have","A","Pen", sep="\n")         # I\nHave\nA\nPen
# print("I","Have","A","Pen", sep="\t")         # I   Have    A   Pen
# print("I","Have","A","Pen", sep=", ")         # I, Have, A, Pen
# print("I","Have","A","Pen", sep=" temp ")     # I temp Have temp A temp Pen


# 4-2. end활용
# print("I")
# print("Like")
# print("Pen")

# print("I", end=" ")
# print("Like", end=" ")
# print("Pen", end=" ")
# => I Like Pen

#직접 바꿔보기
# print("I", end="")
# print("Like", end="")
# print("Pen", end="")


# 5. 연산자
a = 3
b = 2

# print(a + b)      # 3 + 2 = 5
# print(a - b)      # 3 - 2 = 1
# print(a * b)      # 3 * 2 = 6
# print(a / b)      # 3 / 2 = 1.5
# print(a // b)     # 3 // 2 = 1 (몫 구하기)
# print(a % b)      # 3 % 2 = 1 (나머지 구하기)
# print(a ** b)     # 3 ** 2 = 9 (제곱)

# a++, a-- 없음
# +=, -=, *=, /= 대입연산자는 있음

a = 2.0
b = 1

# print(a + b)      # 3.0
# print(a - b)      # 1.0
# print(a * b)      # 2.0
# print(a / b)      # 2.0



# 6. 비교연산자와 불린(bool)

"""
<, >, <=, >=, ==, != 등등 C언어와 같음

bool : 불대수라고도 하고 불린이라고도 하는데 원하는걸로 부르면 됨
참 거짓 두가지 값을 가지고 있음
True == 1, False == 0
으로 알고 있으면 됨
조건문에서 많이 보일 거임 (True가 참, False가 거짓)
조건문이 True일경우 if문 실행, 조건문이 False인 경우 else문 실행(if문 실행 X) 
"""

a = 3
b = 2
c = a == b
d = a != b
# print(c, d)        #False, True

x = 10
y = 20

# print(x > y)        # False
# print(x < y)        # True
# print(x >= y)       # False
# print(x <= y)       # True

# 나중에 실행 해보기
# print(True)
# print(False)