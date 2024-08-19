arr = [-3, -2, -1, 0, 3, 4, 5, 7]

# Brute force approach which has time complexity: O(N)
# for i in range(len(arr)):
#     if arr[i] == 14:
#         print(True)

# BS:
# => Divide the arr into two part and according to value find it

# => I want to find 4
# Steps for BS:
# first we take two points Left and right
# we start while loop and find mid index
# then we compare and find

# TC: O(log N)

def bs(arr,target):
    N = len(arr)

    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

print(bs(arr,0))