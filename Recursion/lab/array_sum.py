def recursive_arr_sum(arr, i=0):
    if i == len(arr) - 1:
        return arr[i]
    return arr[i] + recursive_arr_sum(arr, i + 1)


print(recursive_arr_sum(list(map(int, input().split()))))