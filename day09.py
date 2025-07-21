# 2중 딕셔너리
students = {
    "철수": {"math": 80, "english": 90, "science": 85},
    "민지": {"math": 75, "english": 70, "science": 80},
    "돌쇠": {"math": 90, "english": 85, "science": 95}
}


# for name in students:
#     for subject in students[name]:
#         print(students[name][subject], name, subject)

# 각 학생이 가장 잘본 과목을 출력하시오
# max함수 없이

for i in students:
    subject_list = list(students[i].keys())
    max_score = students[i][subject_list[0]]
    max_subject = ""

    for subject in subject_list:
        if students[i][subject] > max_score:
            max_score = students[i][subject]
            max_subject = subject

    print(f"{i}이(가) 가장 잘본 과목 : {max_subject}")

