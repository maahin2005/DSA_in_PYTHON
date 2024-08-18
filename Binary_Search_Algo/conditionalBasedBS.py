arr = [False, False, False, True, True, True, True]

def findFirstTrue(arr):
    N = len(arr)

    L = 0
    R = N - 1

    while L < R:
        mid = (L + R) // 2

        if arr[mid]:
            R = mid
        else:
            L = mid + 1
    
    return L

print(findFirstTrue(arr))