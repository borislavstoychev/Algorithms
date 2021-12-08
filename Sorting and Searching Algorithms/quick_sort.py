#Избираме пивот и местим всички елементи по малки от него в ляво, а по големите в дясно.
# Mempry: O(log(n)) stack space(recursion)
#Time: O(n**)
# Stable: Depends
# Method: Partitioning

def quick_sort(arr, start= 0, end=6):
    piivot = start
    left = piivot +1 
    right = end
    if start >= end:
        return

    while left <= right:
        if arr[left] > arr[piivot] and arr[right] < arr[piivot]:
            arr[left], arr[right] = arr[right], arr[left]
        
        if arr[left] <= arr[piivot]:
            left += 1

        if arr[right] >= arr[piivot]:
            right -= 1
    arr[piivot], arr[right] = arr[right], arr[piivot]
    smaller_left_sub = right - 1 - start < end - (right + 1)
    if smaller_left_sub :
        quick_sort(arr, start, right -1)
        quick_sort(arr, right + 1, end)

    else:
        quick_sort(arr, right + 1, end)
        quick_sort(arr, start, right - 1)
    return arr
    


print(quick_sort([12, 14, 10, 5, 6, 4, 7]))