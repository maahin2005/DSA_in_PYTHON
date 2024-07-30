# You are given an array of N integers and a single integer K. 
# You need to find out if there is a subarray, which has the sum exactly as K.

K = 5
arr = [1, 2, 3, 1]
N = len(arr)


# step 1: Find the sub-array
# step 2: Find the sum of that sub-array
# step 3: Find the sum that is exactly equal to K 

# step 1:

def solve(arr, N, K):
    for i in range(N):
        for j in range(i,N):
            # step 2:
            sum_ = sum(arr[i:j+1])
            # step 3:
            if sum_ == K:
                return print("YES")
    
    return print("NO")

solve(arr, N, K)