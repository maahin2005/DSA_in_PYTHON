nums = [1, 2, 3]

n = len(nums)
res, sol = [], []

def subsets(i):
    if i == n:
        res.append(sol[:])
        return
    
    # Don't pick number
    subsets(i+1)


    # pick number
    sol.append(nums[i])

    subsets(i+1)

    sol.pop()

subsets(0)
print(res)

# Time Complexity: O(2^N)
# Space Complexity: O(N) + call stack


