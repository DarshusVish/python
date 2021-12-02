list1 = [1,2,3,4,5,6,7,9]

plist = [x for x in range(1,100)]

print(plist, len(plist))
print(list1, len(list1))

list1.sort()
print(list1, len(list1))

def missing(lista):
    ll = []
    for p in plist:
        if not plist[p-1] in lista:
            ll.append(plist[p-1])
            print("Missing item: ",plist[p-1])
    return ll

for i in list1:
    if i < len(list1)-1:
        if list1[i]+1 != list1[i+1]:
            print("missing",list1[i+1]-1,"from",list1)

def getMissingNo(A):
    n = len(A)
    print("lenth of list: ",n)
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(A)
    print("total: ",total)
    print("Sum of all ele from list: ",total)
    return total - sum_of_A

print(getMissingNo(list1))

ad = [x for x in range(1,100)]

ad.pop(49)
ad.pop(49)
print(ad)
print("new",getMissingNo(ad))
print("new func",missing(ad))