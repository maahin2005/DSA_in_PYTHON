# *
# * * 
# * * * 
# * * * *
# * * * * *

N = 5

for row in range(1,N+1):    
    for col in range(row):
        print("*",end=" ")
    print()

# how many Loops: TC: O(N^2)
# O(N) = space constant

# row: 0 to 4 
# 1st Iteration:
# row 2 and col : 0 to 4 

# in row bag = ""

# col loop is running: 1. bag += "* " (bag = "* ")
# col loop is running: 2. bag += "* " (bag = "* *  ")
# col loop is running: 3. bag += "* " (bag = "* * * ")
# col loop is running: 4. bag += "* " (bag = "* * * * ")
# col loop is running: 5. bag += "* " (bag = "* * * * * ")
# row 1st oteration is done: bag = * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 




