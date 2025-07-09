names = ["일창룡", "이창룡", "삼창룡", "사창룡", "오창룡"]

# 값을 하나씩 가져오는거
# for name in names:
#     print(name)

# 인덱스를 하나씩 가져오는거
# for index in range(len(names)):
#     print(index, names[index])

# 인덱스, 값 하나씩 가져오는거
# for index, value in enumerate(names):
#     print(index, value)

# 1부터 n까지의 값을 더한결과를 출력하기
'''
n = int(input("번호를 입력하시요"))

sum = 0
for i in range(1, n+1):
    sum += i
    
print(sum)
'''

# 1부터 100까지의 숫자중에서 3의 배수만 출력하기
# 단, 숫자 와 숫자 사이는 스페이스로 구분한다

# for i in range(1,101):
#     if i % 3 == 0:
#         print(i, end=" ")

# print(*list(range(3,101,3)))

# 1부터 100사이에 입력받은 숫자만 띄우기

n = int(input())
success = False

for i in range(1,101):
    if i == n:
        print(f"입력하신 숫자는 {i} 입니다")
        success = True

if not success:
    print("값이 너무 크거나 작습니다")


