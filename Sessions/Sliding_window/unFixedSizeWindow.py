arr = [4,5,7,2] 

def find_subArr(N):
    for i in range(N):
        for j in range(i+1,N+1):
            print(arr[i:j])

find_subArr(len(arr))