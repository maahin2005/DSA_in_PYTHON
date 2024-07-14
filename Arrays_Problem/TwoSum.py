#EASY
# Two Sum: Given an array of integers, return indices of the two numbers such that they add up to a specific target.

arr = [5,2,5,3,4,5,7,8,9]
N = len(arr)
target = 9

# Brute Force:

for i in range(N):
    flag = False
    for j in range(i+1,N):
        sum_ = arr[i] + arr[j]
        if sum_ == target:
            print(i,j)
            flag = True
            break
    if flag:
        break

# Optimized:

def two_sum(arr, target):

    num_dict = {}

    for i,num in enumerate(arr):

        complement = target - num

        if complement in num_dict:
            return [num_dict[complement],i]
        

        num_dict[num] = i
    return -1

print(two_sum(arr, target))


