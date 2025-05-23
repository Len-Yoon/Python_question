import random
import time

# 1. 10,000개 더미 데이터 생성 (중복 없는 정수, 비정렬 상태)
original_data = random.sample(range(1, 20000), 10000)

### 2. 정렬 알고리즘 구현 (비교 횟수, 교환 횟수 추적) ###

## 선택 정렬 ##
def selection_sort(arr):
    comp = 0
    swap = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comp += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swap += 1
    return comp, swap

## 버블 정렬 ##
def bubble_sort(arr):
    comp = 0
    swap = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            comp += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap += 1
                swapped = True
        if not swapped:
            break
    return comp, swap

## 삽입 정렬 ##
def insertion_sort(arr):
    comp = 0
    swap = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0:
            comp += 1
            if key < arr[j]:
                arr[j+1] = arr[j]
                swap += 1
                j -= 1
            else:
                break
        arr[j+1] = key
    return comp, swap

## 퀵 정렬 ##
def quick_sort(arr):
    comp = [0]
    swap = [0]
    def _quick_sort(array, start, end):
        if start >= end:
            return
        pivot = array[end]
        low = start
        high = end-1
        while low <= high:
            comp[0] += 1
            if array[low] <= pivot:
                low += 1
            else:
                array[low], array[high] = array[high], array[low]
                swap[0] += 1
                high -= 1
        array[low], array[end] = array[end], array[low]
        swap[0] += 1
        _quick_sort(array, start, low-1)
        _quick_sort(array, low+1, end)
    _quick_sort(arr, 0, len(arr)-1)
    return comp[0], swap[0]

### 3. 정렬 알고리즘 성능 비교 ###
sorting_algorithms = [
    ("선택 정렬", selection_sort),
    ("버블 정렬", bubble_sort),
    ("삽입 정렬", insertion_sort),
    ("퀵 정렬", quick_sort)
]

print("===== 정렬 알고리즘 성능 비교 =====")
for name, algorithm in sorting_algorithms:
    data_copy = original_data.copy()
    start_time = time.time()
    comp, swap = algorithm(data_copy)
    end_time = time.time()
    print(f"\n## {name} 결과 ##")
    print(f"소요 시간: {end_time - start_time:.6f}초")
    print(f"비교 횟수: {comp:,}번")
    print(f"교환 횟수: {swap:,}번")
    print(f"정렬 검증: {data_copy == sorted(original_data)}")

### 4. 퀵 정렬로 데이터 정렬 (다음 단계에서 사용) ###
data = original_data.copy()
quick_sort(data)  # 실제 정렬 수행

# 5. 해시 탐색용 딕셔너리 생성 (key: 값, value: 인덱스)
hash_table = {key: idx for idx, key in enumerate(data)}

# 6. 탐색 경로 기록용 배열 준비 (출력용)
sequential_path = []
binary_path = []
interpolation_path = []
hash_path = []

# 7. 순차 탐색 함수 (Sequential Search)
def sequential_search(arr, target):
    count = 0
    path = []
    for i, val in enumerate(arr):
        path.append(val)
        count += 1
        if val == target:
            return i, count, path
    return -1, count, path

# 8. 이진 탐색 함수 (Binary Search)
def binary_search(arr, target):
    start, end = 0, len(arr) - 1
    count = 0
    path = []
    while start <= end:
        mid = (start + end) // 2
        path.append(arr[mid])
        count += 1
        if arr[mid] == target:
            return mid, count, path
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1, count, path

# 9. 보간 탐색 함수 (Interpolation Search)
def interpolation_search(arr, target):
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

# 10. 해시 탐색 함수 (Hash Search)
def hash_search(hash_table, target):
    count = 0
    path = []
    if target in hash_table:
        path.append(target)
        count = 1
        return hash_table[target], count, path
    else:
        count = 1
        return -1, count, path

# 11. 테스트할 값 선택 (랜덤)
search_value = data[random.randint(0, 9999)]

# 12. 각 탐색별 시간 측정 및 결과 출력

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

# 13. 결과 출력 (경로는 너무 길면 일부만 출력)
print("\n===== 탐색 알고리즘 성능 비교 =====")
print(f"찾는 값: {search_value}\n")
print(f"순차 탐색: 인덱스={seq_idx}, 비교 횟수={seq_count}, 시간={seq_time:.6f}초")
print(f"탐색 경로(앞 10개): {sequential_path[:10]}... (총 {len(sequential_path)}개)")

print(f"\n이진 탐색: 인덱스={bin_idx}, 비교 횟수={bin_count}, 시간={bin_time:.6f}초")
print(f"탐색 경로: {binary_path}")

print(f"\n보간 탐색: 인덱스={int_idx}, 비교 횟수={int_count}, 시간={int_time:.6f}초")
print(f"탐색 경로: {interpolation_path}")

print(f"\n해시 탐색: 인덱스={hash_idx}, 비교 횟수={hash_count}, 시간={hash_time:.6f}초")
print(f"탐색 경로: {hash_path}")
