# 1. 변수이름
'''
변수 이름지어줄때 두가지 방법이 있음
스네이크, 카멜
파이썬은 스네이크

helloworld
스네이크 : hello_world
카멜 : helloWorld
'''


# 2. 리스트
'''
배열 VS 리스트

배열 : 길이고정, 동일타입
리스트 : 길이 변경 가능, 서로 다른 타입도 다 가능
'''

# 2-1. 리스트 선언방법
li = list()
# print(li)
li = [1, 2, 3, "1", [1, 2, 3], "hello", 1.1]
# print(li)

# 출력해보기
# print(li[3])          # 1
# print(li[4])          # [1, 2, 3]
# print(li[5])          # hello
# print(li[4][1])       # 2
# print(li[5][2])       # l
# print(li[1][3])       # TypeError
# print(li[7])          # IndexError
# print(li[-8])         # IndexError

# 출력해보기
# print(type(li[3]))        # str
# print(type(li[4]))        # list
# print(type(li[5]))        # str
# print(type(li[4][1]))     # int
# print(type(li[5][2]))     # str

# print(li[:4])
# print(li[::2])
# print(li[-1])

# 2-2. len() <== 길이를 반환해주는 애
li1 = [1, 2, 3, 4]
li2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], 0]
# print(len(li1), len(li2)) # 리스트도 한개의 요소

# 2-3. 리스트 복사
li = [1, 2, 3, 4, 5, 6]
cp_li = li
# print(li, cp_li)

cp_li[0] = 100
# print(li, cp_li, sep="\n") #li, cp_li는 같은 리스트 객체를 보고 있음

# 리스트 복사 방법
cp_li = li[:]
# print(cp_li is li)    # False(같은 리스트를 보고 있지 않음)
# print(cp_li == li)    # True(같은 값을 가지고 있음)


# 3. 리스트 메소드(추가, 삭제) 활용(모든 메소드들은 직접 사용해보기)
animals = ["cat", "dog", "bird"]
# print(animals) # 모든 메소드의 실행 결과는 해당 값을 기준으로 함

# 3-1. append(요소 추가)
# animals.append("tutle")
# print(animals)
# => ["cat", "dog", "bird", "tutle"]
# append 메소드는 리스트에 끝부분에 새로운 요소를 추가해줌

# 3-2. insert(요소 삽입)
# animals.insert(1, "rabbit")
# print(animals)
# => ["rabbit", "cat", "dog", "bird"]
# insert 메소드는 리스트에 원하는 위치에 새로운 요소를 추가해줌
# 단, 원래 위치에 있던 요소와 그 뒤에 있는 요소들은 한칸씩 뒤로 이동함

# animals.insert(10, "rabbit")
# print(animals)
# => ["cat", "dog", "bird", "rabbit"]
# 인덱스가 리스트보다 클 경우 가장뒤에 추가됨

# 3-3. pop(지우기, 지운 값 반환)
# popdata = animals.pop()
# print(animals, popdata)
# => ["cat", "dog"], bird
# pop 메소드는 리스트의 가장 마지막 요소를 제거하고, 제거된 값을 리턴해줌

# popdata = animals.pop(1)
# print(animals, popdata)
# => ["cat", "bird"], dog
# 인덱스를 적어주면 해당 인덱스에 있는 값을 제거하고 리턴해줌
# 단, 인덱스가 리스트의 길이보다 클경우 IndexError발생

# 3-4. remove(지우기, 지운 값 반환 X)
# popdata = animals.remove()
# print(animals, popdata)
# => ["dog", "bird"], None
# remove 메소드는 리스트의 원하는 값을 제거만 하고, 제거된 값을 리턴해주지 않음
# 단, 지우고 싶은 값을 적지 않거나, 지우고 싶은 값이 리스트에 없는 경우 에러 발생

# 3-5. 유효성 검사법

# 3-5-1 remove 유효성 검사
# target = "human"
# if target in animals:
#     popdata = animals.remove("human")
#     print(animals, popdata)
# else:
#     print(f"{target} 없음")

# 3-5-2 pop 유효성 검사
# target = 20
# if target < len(animals):
#     popdata = animals.pop(20)
#     print(animals, popdata)
# else:
#     print(f"{target} 인덱스 사용 불가")

# 3-ex. del 함수(한번씩 주석 풀어서 실행 해보기)
drinks = ["coke", "sprite", "juice", "milk", "fanta",
          "dr.pepper", "milk", "water"]
# print(drinks)

# del drinks[2]
# print(drinks)

# del drinks[-3]
# print(drinks)

# del drinks[:2]
# print(drinks)

# del drinks[:]
# print(drinks)

# index out of range
# del drinks[10]
# print(drinks)


# 3. 리스트 메소드(정렬, 뒤집기) 활용(모든 메소드들은 직접 사용해보기)

arr_int = [1, 4, 5, 2, 3]
arr_str = ['a', 'c', 'd', 'e', 'b']
print(arr_int)
print(arr_str)

# 3-1. sort(정렬)

# 3-1-1. 오름차순
# arr_int.sort()
# arr_str.sort()
# print(arr_int)
# print(arr_str)

# 3-1-2. 내림차순
# arr_int.sort(reverse=True)
# arr_str.sort(reverse=True)
# print(arr_int)
# print(arr_str)

# 3-2. sorted 함수

# 3-2-1. 오름차순
# print(sorted(arr_int))
# print(sorted(arr_str))

# 3-2-2. 내림차순
# print(sorted(arr_int, reverse=True))
# print(sorted(arr_str, reverse=True))

# 3-3. reverse 함수
# arr_int.reverse()
# arr_str.reverse()
# print(arr_int)
# print(arr_str)
