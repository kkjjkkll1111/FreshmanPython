# toeic = int(input("토익점수 : "))
# age = int(input("나이 : "))
# height = int(input("신장길이 : "))
# temp = int(input("경력(연도) : "))
# grade = input("학력 : ")


# 토익점수 900이상, 나이는 30세 미만
'''
if toeic >= 900 and age < 30:
    print("합격")
else:
    print("불합격")
'''

# 토익점수가 950이상이거나, 경력이 5년 이상
'''
if toeic >= 950 or temp >= 5:
    print("합격")
else:
    print("불합격")
'''

# 토익점수가 880이상이거나 나이가 30세 미만인 5년차 경력자
'''
if toeic >= 880 or age < 30 and temp >= 5:
    print("합격")
else:
    print("불합격")
'''

# 학력이 중졸이 아닌 사람
'''
if grade != "중졸":
    print("합격")
else:
    print("불합격")
'''

# select_list = ['a', 'b', 'c', 'd', 'q']
#
# alpha = input("알파벳 하나").lower()
'''
if alpha in select_list:
    print("정상작동")
else:
    print("error")
'''
