# find maximum sum of subArr

arr = [2,3,5,7,8,10]
# in sliding window we have to exclude 1st element of window and move further to the next one element of array
# old window sum =  10 => el = 2 3 5 = 10 - 2 = 8
# ws= 8 + 7 =
# new window sum = 15 => ele = 3 5 7


N = len(arr)

def sum_with_fix_window(N,size):
    if N < size: return "Invalid"

    sum_ = 0

    for i in range(N-size+1):
        sum_ = sum(arr[i:i+size])
        print(sum_)

# sum_with_fix_window(N,2)

def advance_technique(N,size):
    if N < size: return "Invalid"

    window_sum = sum(arr[:size])

    max_sum = window_sum
    
    for i in range(N-size):
        window_sum = window_sum - arr[i] + arr[i+size]
        max_sum = max(max_sum,window_sum)
    
    print(max_sum)
        

advance_technique(N,3)

# i = 0, end of i = 6-2 = 4
# 0, 1, 2, 3

# ws = 5 , ms = 5
# ws = 5 - 2 + arr[i+size] = 0+3 = 3

