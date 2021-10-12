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
