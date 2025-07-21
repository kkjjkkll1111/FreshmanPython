#딕셔너리 = 사전

'''
1. 영어사전

영어단어 : 뜻
apple : 사과
키 : 벨류

2. 연락처
누구 연락처인지 모름

홍길동 : 010-1234-1234
엄복동 : 010-8888-8888
신세계 : 010-7893-7788

이름 : 키
연락처 : 벨류

딕셔너리 : 키, 벨류쌍으로 이루어진 자료형
'''

dict1 = {}
dict2 = dict()
# print(dict1, dict2)

fruits = {
    "apple": 4000,
    "pear": 4500,
    "mango": 4500,
    "peach": 4000,
    "strawberry": 5000
}

# print(fruits)
# print(type(fruits))

print(fruits["apple"], fruits["mango"])

#키로 벨류 가져오는 방법 : 2가지
# dict["key"] vs dict.get("key")
# 에러가 터짐 vs None값으가지냐

# print(fruits["orange"]) # 에러
# print(fruits.get("orange")) # None

# if "orange" not in fruits.keys():
#     print("해당 과일이 없습니다.")

# if not fruits.get("orange"):
#     print("해당 과일이 없습니다.")

# 딕셔너리에 값을 추가하는 방법

subject_scores = {
    "국어": 99,
    "수학": 89,
    "영어": 100
}
print(subject_scores)

subject_scores["한국사"] = 50
subject_scores["물리II"] = 48
subject_scores["지구과학II"] = 47

print(subject_scores)

# 딕셔너리에 값을 수정하는 방법

#수학점수에 오류났음
#수학 점수를 89 -> 93으로 수정
subject_scores["수학"] = 93
print(subject_scores)

#딕셔너리의 키를 삭제하는 방법

# 1. del()
del(subject_scores["한국사"])
print(subject_scores)

# 2. pop()
subject_scores.pop("물리II")
print(subject_scores)

# 3. clear() -> 전부 삭제
subject_scores.clear()
print(subject_scores)



# 반복문과 딕셔너리
smaple = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3",
    "key4" : "value4"
}

for i in smaple: #<--- 딕셔너리의 키를 하나씩 가져옴
    print(smaple[i])

print("="*40)

for i in smaple.keys(): #<--- 딕셔너리의 키를 하나씩 가져옴
    print(i)

print("="*40)

for i in smaple.values(): #<--- 딕셔너리의 벨류를 하나씩 가져옴
    print(i)

print("="*40)

for i in smaple.items(): #<--- 딕셔너리의 키벨류쌍을 하나씩 가져옴
    print(i)

print("="*40)

for k, v in smaple.items(): #<--- 딕셔너리의 키벨류쌍을 하나씩 가져옴
    print(k, v)