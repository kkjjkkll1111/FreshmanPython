# 조건문

# a = int(input("값 1 :").strip())
# cal = input("연산자 : ").strip()
# b = int(input("값 2 : ").strip())
#
# result = 0
# right_cal = True
#
# if cal == '+':
#     result = a + b
# elif cal == '-':
#     result = a - b
# elif cal == '*':
#     result = a * b
# elif cal == '/':
#     if b == 0:
#         right_cal = False
#     else:
#         result = a / b
# else:
#     right_cal = False
#
#
# if right_cal:
#     print(f"{a} {cal} {b} = {result}")
# else:
#     print("오류가 발생하였습니다")



# 성적처리하는 코드
# 100~90 : A, 89~80 : B, 79~70 : C, 69~60 : D, 59~0: F
# 0이하, 100이상이면 오류
# 단, 문자를 입력하는 경우는 제외

score = int(input("점수를 입력하세요").strip())
grade = ''

if (score >= 0) and (score <= 100):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
else:
    grade = 'err'

if grade == 'err':
    print("점수에 이상이 있습니다")
else:
    print(f"당신의 등급은 {grade}등급입니다")

