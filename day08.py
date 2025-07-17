#딕셔너리

#정보(리스트)
info = ["오창룡", 21, "남", 175.9, 53.2, ["사과", "딸기", "바나나"]]
# print(f"이름 : {info[0]}")
# print(f"나이 : {info[1]}")
# print(f"키 : {info[3]}")

#정보(딕셔너리)
info = {
    "이름": "오창룡",
    "나이": 21,
    "성별": "남",
    "키": 175.9,
    "몸무게": 53.2,
    "좋아하는 과일": ["사과", "딸기", "바나나"]
}
# print(f"이름 : {info["이름"]}")
# print(f"나이 : {info["나이"]}")
# print(f"키 : {info["키"]}")



a = {"key1": 100, "key2": 200, "key3": 300}
# print(a)
# print(a["key2"])

scores = {
    "kor": 90,
    "math": 45,
    "eng": 92
}
# print(scores)
#추가
scores["science"] = 75
# print(scores)

#수정
scores["math"] = 62
# print(scores)

#키값이 딕셔너리 안에 없으면 추가가 되고, 있으면 수정이 됨

#삭제
del(scores["science"])
# print(scores)

#삭제 유효성 검사
# target = "history"
# if target in scores:
#     del(scores[target])
#     print(scores)
# else:
#     print("키가 존재하지 않음")

# for key, value in scores.items():
#     print(f"{key} : {value}점")

# for key in scores:
#     print(f"{key} : {scores[key]}점")

game_scores = {
    "민수": 9874582,
    "재원": 8879285,
    "하은": 9889748
}

# 가장 점수가 낮은 사람의 이름을 출력
# min함수 없이

user_list = list(game_scores.keys())

min_score = game_scores[user_list[0]]
min_user = ""
for user, score in game_scores.items():
    if min_score > score:
        min_score = score
        min_user = user

print(f"점수가 가장낮은 유저 : {min_user}")


