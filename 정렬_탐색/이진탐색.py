def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid  # 찾은 경우 인덱스 반환
        elif arr[mid] < target:
            start = mid + 1  # 오른쪽 절반 탐색
        else:
            end = mid - 1    # 왼쪽 절반 탐색
    return -1  # 찾지 못한 경우

# 사용 예시
arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(arr, 7))   # 출력: 3 (7의 인덱스)
print(binary_search(arr, 2))   # 출력: -1 (2는 없음)
