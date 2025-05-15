def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= x <= arr[high]:
        # 분모가 0이 되는 경우 방지
        if arr[high] == arr[low]:
            if arr[low] == x:
                return low
            else:
                break

        # 예상 위치 계산
        pos = low + ((x - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# 사용 예시
arr = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
print(interpolation_search(arr, 33))  # 출력: 6 (33의 인덱스)
print(interpolation_search(arr, 100)) # 출력: -1 (없음)