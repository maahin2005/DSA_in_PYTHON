# Count the pair which sum is up to K

arr = [1, 4, 4, 5, 5, 5, 6, 6, 11]
K = 11
N = len(arr)
count = 0

def Count_pairs(arr,n,k):

    global count
    i = 0
    j = n-1

    while(i<j):
        sum_ = arr[i] + arr[j]

        if sum_ == k:
            count += 1
            left = i + 1
            right = j - 1

            while left < j and arr[left]==arr[i]:
                count += 1
                left += 1

            while right > i and arr[right]==arr[j]:
                count += 1
                right -= 1

            i += 1
            j -= 1    

        elif sum_ > k:
            j-=1
        else:
            i+=1

Count_pairs(arr,N,K)
print(count)