def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr

def bubble_sort2(arr):
    is_sorted = False
    count = 0
    while not is_sorted:
        is_sorted = True
        for i in range(1, len(arr) - count):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                is_sorted = False
    return arr 


print(bubble_sort2([3, 2, 8, 1, 6, 6, 8]))