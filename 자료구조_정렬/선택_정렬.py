def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


arr = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print(selection_sort(arr))  ##[1, 2, 3, 4, 5, 6, 7, 8, 9]