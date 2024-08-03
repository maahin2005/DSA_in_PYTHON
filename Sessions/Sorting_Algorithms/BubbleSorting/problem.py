arr = [2, 3, 99, 80, 35, 100]
N = len(arr)

for i in range(N):
    swapped = False
    for j in range(N-1-i):
        if arr[j+1] < arr[j]:
            arr[j] , arr[j + 1] = arr[j+1], arr[j]
            swapped = True
    
    if not swapped:
        break

print(arr)