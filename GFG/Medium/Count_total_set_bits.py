print("--------------------------------------------")

n=4
count = 0
for i in range(0,n+1):
    while i>1:
        if(i%2==1):
            count = count+1
        i=i//2
    if(i==1):
        count = count+1

print(f"n is: {i}\nCount: {count}" )

print("--------------------------------------------")


# Input: 
# n = 4
# Output: 5
# Explanation: 
# For numbers from 1 to 4. 
# For 1: 0 0 1 = 1 set bits 
# For 2: 0 1 0 = 1 set bits 
# For 3: 0 1 1 = 2 set bits 
# For 4: 1 0 0 = 1 set bits 
# Therefore, the total set bits is 5.

# --------------------------------------------
# n is: 1
# Count: 5
# --------------------------------------------
