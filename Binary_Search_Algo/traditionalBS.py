arr = [-5, -3, -2, 1, 3, 5]

def binary_search(arr,val):
    n = len(arr)

    left = 0
    right = n - 1

    while left <= right:
        mid = left + (right-left//2)

        if arr[mid] == val:
            return True
        elif arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    
    return False


print(binary_search(arr,15))