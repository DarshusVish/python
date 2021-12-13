
def mindiff(n,arr):
    arr.sort()
    x = arr[1] - arr[0]
    print(arr)
    for i in range(len(arr)-1):
        if (arr[i+1]-arr[i]) == x:
            print(arr[i],arr[i+1])

n=4
arr = [4,3,2,1]
mindiff(n,arr)

from Test1.pack1.fact import facto
print(facto(5))


from Test1.pack2.fibbb import fib
x = [fib(x) for x in range(10)]
print(x)