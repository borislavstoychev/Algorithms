#Разбиваме масива на половина докато в него остане един елемент.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    merged = []
    merge_index = 0
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
        merge_index += 1
    
    while left_index < len(left) :
        merged.append(left[left_index])
        left_index += 1
        merge_index += 1

    while right_index < len(right) :
        merged.append(right[right_index])
        right_index += 1
        merge_index += 1

    return merged

#second solution 
def merge_sort2(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]

        # Recursive call on each half
        merge_sort2(left)
        merge_sort2(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # The value from the left half has been used
                my_list[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1


myList = list(map(int, input().split()))
print(*merge_sort(myList), sep=" ")
merge_sort2(myList)
print(myList)