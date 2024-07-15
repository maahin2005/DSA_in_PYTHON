# You are given a string, you have to find the count of all such substrings which start and end with same character

string = "ababa"

def Solve(S):
    # Step 1: Count frequency of each character
    freq = {}

    for char in S:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Step 2: Calculate substrings for each character
    count = 0
    for char in freq:
        f = freq[char]

        # Using the formula to calculate the number of substrings 
        count += (f * (f + 1)) // 2

    return count

print(Solve(string))


