def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


my_list = [45, 2, 15, 29, 0, 12, 67, 20]
print(my_list)
print(bubble_sort_desc(my_list))
