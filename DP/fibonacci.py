n = 1
dp = [-1] * (n+1)
def f(n,dp):
    if n <= 1:
        return n
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = f(n-1,dp) + f(n-2,dp)

    return dp[n]

print(f"{n}th fib is {f(n,dp)}")

# Bottom Up Approach:

def solve(n):
    if n <= 1:
        return n

    dp=[0]*(n+1)

    dp[1]=1

    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[n]

print(solve(n))