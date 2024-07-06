# Prime Substring 

string = "abcdef"
N = len(string)

# Step 1: Find Out the Sub Strings
# step 2: check the sub string length is Prime or not
# step 3: latly count the all substring whichever length has Prime

def isPrime(num):
    if num <= 1:
        return False
    
    for i in range(2,num):
        if num % i == 0:
            return False
        
    return True

countPrimeLen = 0

# step 1:
for i in range(N):
    for j in range(i,N):
        # step 2:
        isTrue = isPrime(len(string[i:j+1]))
        # step 3:
        if isTrue:
            countPrimeLen += 1

print(countPrimeLen)