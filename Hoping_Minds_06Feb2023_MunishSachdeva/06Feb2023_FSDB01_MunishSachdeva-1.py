# arr.sort()
# print(arr)

def bubble(arr):
    has_swapped = True
    while(has_swapped):
        has_swapped = False
        n = len(arr)
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                has_swapped = True
            print(f'step {i} {arr}')
        print()
                # temp = arr[i]
                # arr[i] = arr[i+1]
                # arr[i+1] = temp
                # i = i+1
    return arr

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
arr3 = [5, 6, 4, 3, 1, 2, 7, 8, 9, 10]

print(bubble(arr1))
print(bubble(arr2))
print(bubble(arr3))

