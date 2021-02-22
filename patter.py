n = int (input("Enter the number:"))
# n =int(n/2)
print("Value of n is :",n)
k=1
for i in range(1, n+1):
    print(k, end="")
    for j in range(1, n+1):
        # if(j >= n-(i-1) and j <= n+(i-1)):
        if (i == int(n/2)+1 or j == int(n/2)+1):
        # if (i == (n/2)+1 or j == (n/2)+1 ):
            print(" * ", end="")
        else:
            print("   ",end="")
    k += 1
    print()

# Value of n is : 9
# 1             *
# 2             *
# 3             *
# 4             *
# 5 *  *  *  *  *  *  *  *  *
# 6             *
# 7             *
# 8             *
# 9             *

k = 1
for i in range(1, n+1):
    print(k, end="")
    for j in range(1, n+1):
        if(j >= n-(i-1) and j <= n+(i-1)):
            print(" * ", end="")
        else:
            print("   ",end="")
    k += 1
    print()

# OutPut
# 1             *
# 2          *  *
# 3       *  *  *
# 4    *  *  *  *
# 5 *  *  *  *  *

k = 1
for i in range(1, n+1):
    print(k, end="")
    for j in range(1, 2*n):
        if(j >= n-(i-1) and j <= n+(i-1)):
            print(" * ", end="")
        else:
            print("   ",end="")
    k += 1
    print()

# OutPut
# 1             *
# 2          *  *  *
# 3       *  *  *  *  *
# 4    *  *  *  *  *  *  *
# 5 *  *  *  *  *  *  *  *  *


print()
print()
print()
k = 1
for i in range(1, n+1):
    print(k, end="")
    for j in range(1, 2*n):
        if(j >= n-(i-1) and j <= n+(i-1)):
            print(" * ", end="")
        else:
            print("   ",end="")
    if (k < n):
        k += 1
    print()
k -=1
for i in range(n-1, 0,-1):
    print(k, end="")
    for j in range(1, 2*n):
        if(j >= n-(i-1) and j <= n+(i-1)):
            print(" * ", end="")
        else:
            print("   ",end="")
    k -= 1
    print()

# OutPut
# 1             *
# 2          *  *  *
# 3       *  *  *  *  *
# 4    *  *  *  *  *  *  *
# 5 *  *  *  *  *  *  *  *  *
# 4    *  *  *  *  *  *  *
# 3       *  *  *  *  *
# 2          *  *  *
# 1             *


print("New")

for i in range(1,n+1):
    for j in range(1, n+1):
        if( j >= n-(i-1) and j <= n+(i-1)):
            print(" * ",end="")
        else:
            print("   ", end="")
    print()

for i in range(n-1,0,-1):
    for j in range(1,1*n+1):
        if( j >= n-(i-1) and j <= n+(i-1)):
            print(" * ",end="")
        else:
            print("   ", end="")
    print()

# OutPut
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
