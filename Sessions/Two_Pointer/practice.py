# Problem: find the pair which sum is up to K

arr = [1, 2, 3, 4, 5]

N = len(arr)
K = 7


# Lets discuss Solution:
# we need pair? 2 element
# take a single element and try with other all

# Brute Force Approach:

# for i in range(N-1):
#     for j in range(i+1,N):
#         sum_ = arr[i] + arr[j]
#         if sum_ == K:
#             print("The Ans is: ",arr[i], arr[j])




# Two - Pointer approach

left = 0
right = N - 1
count = 0

while left < right:
    sum_ = arr[left] + arr[right]

    if sum_ == K:
        count+=1
        left+=1
        right-=1
    elif sum_ < K:
        left += 1
    else:
        right -= 1

print(count)
# left = 0 and right = 4
# 0 < 4 true
# sum_ = 1 + 5 = 6
# left += 1; left = 1
# left = 1 and right = 4
# sum_ = 2 + 5 = 7
# left = 2 and right = 3
# sum_ = 3 + 4 = 7
# left = 3 and right = 2