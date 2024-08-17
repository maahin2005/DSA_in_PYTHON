def solve_sum(n):
    
    cnt = n + 1
    print("cnt : ", cnt)

    if cnt == 5:
        return cnt
    return solve_sum(cnt)


cnt = solve_sum(2)
print(cnt)