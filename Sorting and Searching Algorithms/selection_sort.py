# start from begining and swap current index num from first loop with current index from second loop if the number is smaler.
def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


print(selection_sort([5, 4, 7, 8, 3, 2, 6, 1]))