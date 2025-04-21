# 신용카드 번호 만들기 풀이
str = input("신용카드 번호를 입력하세요 (-) 포함")

result = "Valid"
arr = list(str.split("-"))

result = "Invalid" if arr[0][0] not in (4,5,6) else "Valid"
result = "Invalid" if arr[0] == arr[1] == arr[2] == arr[3] else "Valid"

print(result)