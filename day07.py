#while

# break
# count = 0
# print("열 번 찍어 안 넘어가는 나무 없다")
# while True:
#     if count == 10:
#         print("나무가 넘어졌어요~")
#         break
#     count += 1
#     print(f"현재 카운트 :{count}")


# continue
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i,end=" ")

# pass
# a = 10
# if a == 10:
#     pass

# 튜플
# 나중에 정리

# 딕셔너리
a = {
    "이름": "오창룡",
    "나이": 21,
    "키" : 176.1,
    "몸무게": 51.3
}

# 성적 추가
# a["성적"] = ['A+', 'A+', 'A+', 'A+', 'A+', 'A+']
a["키"] = 175.9
# print(a["키"])

scores = {"kor": 98,"math": 100,"eng": 99}

for i in scores.keys(): #keys 생략 가능
    print(i)

for i in scores.values():
    print(i)

for i in scores.items():
    print(i)

