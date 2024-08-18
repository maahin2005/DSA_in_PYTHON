arr = [-5, 3, 2, 1, 0, -2, -3, -3, 7, 5, 2]

def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return arr
    
    m = len(arr)//2
    L = arr[:m]
    R = arr[m:]

    L = merge_sort(L)
    R = merge_sort(R)
    
    l,r = 0,0
    L_len=len(L)
    R_len=len(R)

    sorted_arr = [0]*n
    i = 0

    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:
            sorted_arr[i] = R[r]
            r += 1
        i += 1
    
    while l < L_len:
        sorted_arr[i] = L[l]
        i += 1
        l += 1
    
    while r < R_len:
        sorted_arr[i] = R[r]
        i += 1
        r += 1
    
    return sorted_arr
        
print(merge_sort(arr))


# steps inside merge function:

## PART 1: Spliting arr/ breaking arr => until single element remain
# handle base case => if len of arr is 1 so return curr arr
# find middle index of arr
# create 2 arr left and right => left is half 0 to mid and right is remain half
# now do recursive call with this new left and right arr

## PART 2: start merging arrays
# take 2 index l and r for left and right arrays
# take 2 variables for the left and right arrays
# declare new arr with size n(actual arr size) and filled it with zeros
# take one more index i for new declared arr
# start while loop and compare all elements of right and left arrays and assign them into new declared arr wrt index
# then take 2 while loop for left and right for remianing elements in left amd right arrays