#  Problem - find the sub string 

string = "karan"

N = len(string)

for i in range(N):
    for j in range(i+1, N+1):
        print(string[i:j])

# i loop => 0 to 4
# j loop => i+ 1 to 5

# 1st Iteration of I:
# i = 0 and j = i+1 ; j=1 => N+1 => 6 will exclude and run untile 5

# 1st Iteration of J: i=0, j=1
# string[0:1] = k
# 2nd Iteration of j: i=0, j=2
# string[0:2] = ka
# 3rd Iteration of j: i=0,j=3
# string[0:3] = kar
# 4th Iteration of J: i=0,j=4
# string[0:4] = kara
# 5th Itaration of J: i=0, j=5
# string[0:5] = karan

# 2nd Iteration of I:
# I = 1 and j = 2 (j=2,J=5 ) 2,3,4,5

# 1st Iteration of J: i=1, j =2
# string[1:2] = a



# .......................