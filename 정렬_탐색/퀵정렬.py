## 분할 정복 전략
## 피벗 선택 - 분할 - 재귀적 정렬
## 시간복잡도: 평균 O(n log n), 최악 O(n²)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # 원소가 1개 이하라면 그대로 반환
    pivot = arr[0]  # 첫 번째 원소를 피벗으로 선택
    left = [x for x in arr[1:] if x <= pivot]  # 피벗보다 작거나 같은 값
    right = [x for x in arr[1:] if x > pivot]  # 피벗보다 큰 값
    return quick_sort(left) + [pivot] + quick_sort(right)  # 재귀적으로 정렬 후 결합

arr = [9,5,2,7,4,1,3,6,8]
sorted_arr = quick_sort(arr)
print(sorted_arr)