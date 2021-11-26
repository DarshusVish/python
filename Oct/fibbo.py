# def fib():
#     a,b = 0,1
#     while True:
#         c = a
#         a = b
#         b = c+a
#         yield c
#
# f = fib()
# for i in range(10):
#     print(next(f))

# def fibb(n):
#     return 0 if(n==0)else (1 if(n==1 or n==2) else fibb(n-1) + fibb(n-2))
#
# x = [fibb(x) for x in range(10)]
# print(x)

def fib(n):
    if (n < 1):
        return 0
    if(n<2):
        return 1
    return fib(n-2) + fib(n-1)

x = [fib(x) for x in range(10)]
print(x)