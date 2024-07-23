def getFirstElement(array):
    return array[0]

ans = getFirstElement([1,2,3,4,5]) # Length 5: 1
ans = getFirstElement([10,20,30]) # Length 3: 10
ans = getFirstElement([99]) # Length 1: 99

print(ans)
# Conclusion: No metter whats the lenght of array it will take only first element 
# and perform the task so time complexity is O(1) / constant