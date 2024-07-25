arr = [2,3,5,7,1,8,9,20] # O(N);
# n = len(arr) # O(1)
# for i in range(n):
#     print(arr[i]) 
#O(N)



# def doSum(arr):
#     sum = 0
#     n = len(arr)
#     for i in range(n):
#         sum += arr[i]
    
#     return sum

# print(doSum(arr))

# print(arr,"A") # O(1) 

# Total TC: O(N) + O(1) + O(N) + O(1) = N + 2 + N = 2N + 2 = O(N)
# When we printing anything it's TC most probably O(1) only

# O(log N)

# 2 * 2 * 2 = 8

# log2(8) = 3

# log2(16) = 4

# log2(10) = 2 * 2 * 2 = 3


def printPattern(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or j==(n-1):

                print('*', end=" ")
        print(" ")

printPattern(5)






