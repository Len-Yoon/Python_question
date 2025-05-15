def sequential_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # 값을 찾으면 인덱스 반환
    return -1  # 끝까지 못 찾으면 -1 반환

# 사용 예시
numbers = [17, 92, 18, 33, 58, 7, 33, 42]

print(sequential_search(numbers, 18))   # 2 (18의 인덱스)
print(sequential_search(numbers, 33))   # 3 (33이 두 번 있지만 처음 위치 반환)
print(sequential_search(numbers, 900))  # -1 (900은 리스트에 없음)