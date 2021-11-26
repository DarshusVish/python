def pat(n):

    for i in range(n+1,1,-1):
        for j in range(1,i):
            print(i-1, end=" ")
        print(end="\n")

# pat(5)

def pat1(n):
    for i in range(1,n):
        for j in range(1,n-i+1):
            print(end=" ")
        for j in range(1,i+1):
            print("* ",end="")
        print()

pat1(5)