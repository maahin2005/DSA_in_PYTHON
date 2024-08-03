arr = [100,99,80,35,4,2,10]

N = len(arr)

for i in range(N):
    min_ind = i
    for j in range(i+1,N):
        if arr[j] < arr[min_ind]:
            min_ind = j
    if min_ind != i:
        arr[i] , arr[min_ind] = arr[min_ind],arr[i]

print(arr)