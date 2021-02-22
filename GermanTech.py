x = int(input("Enter a number: "))
c = 0
while True:
    if((x%2)==0):
        x = x /2
        c += 1
    print(int(x))
    
    if (x == 1):
        break
    
    if((x%2)==1):
        x = 3*x + 1
        c +=1
        print(int(x))
    
print("steps: ",c)
