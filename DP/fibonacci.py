n = 4
dp = [-1] * (n+1)
def f(n,dp):
    if n <= 1:
        return n
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = f(n-1,dp) + f(n-2,dp)

    return dp[n]

# TC: O(N) 
# SC: O(N) + call stack O(N)
print(f"{n}th fib is {f(n,dp)}")

# Bottom Up Approach (Tabulation): 
# Reduce the call stack from SC

def solve(n):
    if n <= 1:
        return n

    dp=[0]*(n+1)

    dp[1]=1

    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[n]

# TC: O(N)
# SC: O(N)
print(solve(n))

# Again Try to Reduce the SC:

def fn(n):
    prev_2 = 0
    prev_1 = 1

    for _ in range(2,n+1):
        currI = prev_1 + prev_2
        prev_2 = prev_1
        prev_1 = currI
    
    return prev_1

# TC: O(N)
# SC: O(1)
print(fn(n))