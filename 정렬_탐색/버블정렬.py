## 배열의 처음부터 끝가지 인접한 두 원소 비교
## 앞의 값이 뒤의 값보다 크면 둘의 위치를 교체(오름차순 기준)
## 한 번의 전체 순회가 끝나면 가장 큰 값이 배열의 마지막에 위치
## 이 과정을 배열의 길이만큼 반복합니다. 반복할 때마다 마지막에 정렬된 부분은 제외하고 비교
## 시간 복잡도: 최악/평균 O(n²), 최선(이미 정렬된 경우) O(n)
## 데이터가 많을수록 비효율적

arr = [9,5,2,7,4,1,3,6,8]

n = len(arr)

for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 위치 교환
            swapped = True
        if not swapped:  # 교환이 한 번도 일어나지 않으면 정렬 종료
            break

print(arr)