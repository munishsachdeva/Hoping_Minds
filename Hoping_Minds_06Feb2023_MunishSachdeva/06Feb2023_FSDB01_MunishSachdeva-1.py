
# arr.sort()
# print(arr)
def bubble(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # temp = arr[j]
                # arr[j] = arr[j+1]
                # arr[j+1] = temp
                # j = j+1
            print(f'step {i+1} {arr}')
            #return(arr)
    print()
    return()

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
arr3 = [5, 6, 4, 3, 1, 2, 7, 8, 9, 10]

bubble(arr1)
bubble(arr2)
bubble(arr3)


