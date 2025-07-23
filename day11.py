#함수

def avg(li):
    return sum(li) / len(li)

def add_student(students,stu_no, name):
    if stu_no in students.keys():
        print("이미 존재하는 학번입니다")
        return False
    else:
        students[stu_no] = name
        print("성공적으로 등록이 되었습니다.")
        return True

def remove1(li):
    cpli = li[:]
    if 1 in li:
        cpli.remove(1)
    return cpli

li = [100,200,300,400]
print(len(li))
print(sum(li))
print(max(li))
print(min(li))
print(avg(li))

students = {
    20241111 : "홍길동",
    20241112 : "이순신",
    20241113 : "단군"
}

add_student(students, 20241111, "임꺽정")
add_student(students, 20241114, "임꺽정")
print(students)



li1 = [1, 2, 3, 4]
print(remove1(li1))
print(li1)