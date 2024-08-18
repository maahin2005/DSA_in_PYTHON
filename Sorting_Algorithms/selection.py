arr = [-5, 3, 2, 1, 0, -2, -3, -3, 7, 5, 2]

def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        min_ind = i
        for j in range(i+1,n):
            if arr[min_ind] > arr[j]:
                min_ind = j
        
        if min_ind != i:
            arr[min_ind], arr[i] = arr[i], arr[min_ind]

selection_sort(arr)
print(arr)