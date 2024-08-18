arr = [-5, 3, 2, 1, 0, -2, -3, -3, 7, 5, 2]

# Time Complexity: O(N log N) - Average Case || O(N^2) - worst case (if Pivot is useless)
# Space Complexity: O(N)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]

    L = [x for x in arr[:-1] if x <= pivot]
    R = [x for x in arr[:-1] if x > pivot]
    
    L = quick_sort(L)
    R = quick_sort(R)

    return L + [pivot] + R

print(quick_sort(arr))