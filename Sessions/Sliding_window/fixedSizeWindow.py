arr = [2,3,5,7,8,10]
N = len(arr)

def find_subArr_with_fixed_size(N, size):
    if N < size: return print("Invalid")

    for i in range(N - size + 1):
        print(arr[i:i+size])


find_subArr_with_fixed_size(N, 3)

# debug:
# N = 12 ; size = 3
# Every time we will point our i at index of first element of window

# 1st Iteration:
# i = 0 and end = 9
# arr[i:0+3]=[0,3]=0,1,2=1,2,3
# i = 1
# arr[i:i+size] = [1,4]= 1,2,3 = 2,3,4
# i=9
# arr[i:i+size] = [9,12] = 9,10,11
# i=10
