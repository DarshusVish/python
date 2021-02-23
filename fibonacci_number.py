def fib(n):
    return 1 if (n ==1 or n ==2 )else fib(n-1)+fib(n-2)

for i in range (1,10):
    print(fib(i),end=" ")
