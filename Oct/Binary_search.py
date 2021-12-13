P = -1

def bsearch(list,n):
    l = 0
    u = len(list)-1
    while l <= u:
        mid = (l+u)//2

        if list[mid] == n:
            globals() ['P'] = mid
            return P

        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid+1
    return False


# ll = [x for x in range(1,1000)]
# n = 200
# if bsearch(ll,n):
#     print("Found at",p+1)
# else:
#     print("Not found")
