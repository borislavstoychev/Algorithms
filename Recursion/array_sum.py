def recursive_arr_sum(arr, i=0):
    if i == len(arr) - 1:
        return arr[i]
    return arr[i] + recursive_arr_sum(arr, i + 1)


print(recursive_arr_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))