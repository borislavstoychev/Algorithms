def binary_search(arr,start , end, searching_number):
    while start <= end:
        mid = (start + end)  // 2

        if arr[mid] == searching_number:
            return mid
        elif arr[mid] < searching_number:
            start = mid + 1
        else:
            end = mid - 1

    else:
        return -1 

arr = [2, 3, 4, 10, 40]
x = 10
start = 0
end = len(arr) - 1

# Function call
print(binary_search(arr, start, end, x))








# # Python 3 program for recursive binary search.
# # Modifications needed for the older Python 2 are found in comments.

# # Returns index of x in arr if present, else -1
# def binary_search(arr, low, high, x):
#     # Check base case
#     if high >= low:

#         mid = (high + low) // 2

#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return mid

#         # If element is smaller than mid, then it can only
#         # be present in left subarray
#         elif arr[mid] > x:
#             return binary_search(arr, low, mid - 1, x)

#         # Else the element can only be present in right subarray
#         else:
#             return binary_search(arr, mid + 1, high, x)

#     else:
#         # Element is not present in the array
#         return -1


# # Test array
# arr = [2, 3, 4, 10, 40]
# x = 10

# # Function call
# result = binary_search(arr, 0, len(arr) - 1, x)

# if result != -1:
#     print(arr[result])
# else:
#     print("Element is not present in array")