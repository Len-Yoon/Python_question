import random
import time

# 1. 10,000개 더미 데이터 생성 (중복 없는 정수, 오름차순 정렬)
data = sorted(random.sample(range(1, 20000), 10000))  # 1~19999 중 10,000개 랜덤 추출

# 2. 해시 탐색용 딕셔너리 생성 (key: 값, value: 인덱스)
hash_table = {key: idx for idx, key in enumerate(data)}

# 3. 탐색 경로 기록용 배열 준비 (출력용)
sequential_path = []
binary_path = []
interpolation_path = []
hash_path = []

# 4. 순차 탐색 함수 (Sequential Search)
def sequential_search(arr, target):
    """
    리스트를 처음부터 끝까지 순차적으로 탐색
    :param arr: 탐색할 리스트
    :param target: 찾을 값
    :return: (인덱스, 비교 횟수, 탐색 경로)
    """
    count = 0
    path = []
    for i, val in enumerate(arr):
        path.append(val)     # 경로 기록
        count += 1           # 비교 횟수 증가
        if val == target:
            return i, count, path
    return -1, count, path   # 못 찾으면 -1 반환

# 5. 이진 탐색 함수 (Binary Search)
def binary_search(arr, target):
    """
    정렬된 리스트에서 중간값과 비교하며 탐색 범위를 반씩 줄여가는 방식
    :param arr: 정렬된 리스트
    :param target: 찾을 값
    :return: (인덱스, 비교 횟수, 탐색 경로)
    """
    start, end = 0, len(arr) - 1
    count = 0
    path = []
    while start <= end:
        mid = (start + end) // 2
        path.append(arr[mid])  # 경로 기록
        count += 1
        if arr[mid] == target:
            return mid, count, path
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1, count, path

# 6. 보간 탐색 함수 (Interpolation Search)
def interpolation_search(arr, target):
    """
    데이터가 고르게 분포된 정렬 리스트에서 탐색 위치를 보간 공식으로 계산
    :param arr: 정렬된 리스트
    :param target: 찾을 값
    :return: (인덱스, 비교 횟수, 탐색 경로)
    """
    low, high = 0, len(arr) - 1
    count = 0
    path = []
    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            path.append(arr[low])
            count += 1
            if arr[low] == target:
                return low, count, path
            return -1, count, path
        # 보간 공식으로 pos 계산
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))
        path.append(arr[pos])
        count += 1
        if arr[pos] == target:
            return pos, count, path
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1, count, path

# 7. 해시 탐색 함수 (Hash Search)
def hash_search(hash_table, target):
    """
    딕셔너리의 키로 바로 접근 (O(1))
    :param hash_table: {값: 인덱스} 딕셔너리
    :param target: 찾을 값
    :return: (인덱스, 비교 횟수, 탐색 경로)
    """
    count = 0
    path = []
    if target in hash_table:
        path.append(target)  # 경로 기록 (딕셔너리는 바로 찾으므로 target만 기록)
        count = 1
        return hash_table[target], count, path
    else:
        count = 1
        return -1, count, path

# 8. 테스트할 값 선택 (랜덤)
search_value = data[random.randint(0, 9999)]  # 데이터 내 임의 값

# 9. 각 탐색별 시간 측정 및 결과 출력

# 순차 탐색
start = time.time()
seq_idx, seq_count, sequential_path = sequential_search(data, search_value)
end = time.time()
seq_time = end - start

# 이진 탐색
start = time.time()
bin_idx, bin_count, binary_path = binary_search(data, search_value)
end = time.time()
bin_time = end - start

# 보간 탐색
start = time.time()
int_idx, int_count, interpolation_path = interpolation_search(data, search_value)
end = time.time()
int_time = end - start

# 해시 탐색
start = time.time()
hash_idx, hash_count, hash_path = hash_search(hash_table, search_value)
end = time.time()
hash_time = end - start

# 10. 결과 출력 (경로는 너무 길면 일부만 출력)
print(f"찾는 값: {search_value}\n")
print(f"순차 탐색: 인덱스={seq_idx}, 비교 횟수={seq_count}, 시간={seq_time:.6f}초")
print(f"탐색 경로(앞 10개): {sequential_path[:10]}... (총 {len(sequential_path)}개)")

print(f"\n이진 탐색: 인덱스={bin_idx}, 비교 횟수={bin_count}, 시간={bin_time:.6f}초")
print(f"탐색 경로: {binary_path}")

print(f"\n보간 탐색: 인덱스={int_idx}, 비교 횟수={int_count}, 시간={int_time:.6f}초")
print(f"탐색 경로: {interpolation_path}")

print(f"\n해시 탐색: 인덱스={hash_idx}, 비교 횟수={hash_count}, 시간={hash_time:.6f}초")
print(f"탐색 경로: {hash_path}")