string = "abcdef"
N = len(string)

def isPrime(num):
    if num <= 1:
        return False
    
    for i in range(2,num): 
        if num % i == 0:
            return False
    
    return True


count = 0

for i in range(N):
    for j in range(i+1,N+1):
        subStrLenght = len(string[i:j])
        if isPrime(subStrLenght):
            count += 1

print("count: " , count)

# TC: O(N^3) 
# SC: O(1)