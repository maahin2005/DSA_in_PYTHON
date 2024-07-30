# array = ['k','a','r','a','n']
# N = len(array)

# for i in range(N): 
#     for j in range(i+1,N+1):
#         print(array[i:j])

# TC: O(N^3)
# SC: O(N^3)

K = 3
arr = [1, 2, 3, 1, 4]
N = len(arr)

for i in range(N):
    for j in range(i+1,N+1):
        sumOfSubArray = sum(arr[i:j])
        if (sumOfSubArray == K):
            print(arr[i:j])


