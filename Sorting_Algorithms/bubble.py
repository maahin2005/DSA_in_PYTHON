arr = [-5, 3, 2, 1, 0, -2, -3, -3, 7, 5, 2]

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
        
bubble_sort(arr)
print(arr)
