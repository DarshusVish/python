# Prime number Between numbers

# def PrimeNumSeries(v,d):
#     ll = []
#     for i in range(v,d):
#         if all( i % k != 0 for k in range(2,(int(i**0.5)+1))) and i != 0:
#             ll.append(i)
#     return ll
#
# k = PrimeNumSeries(100,200)
# print(k, len(k))

################################################################################
# bubble sorting
# ll = [3,4,5,6,1,2]
#
# def bsort(list):
#     for k in range(len(list)-1,0,-1):
#         for i in range(k):
#             if list[i] > list[i+1]:
#                 temp = ll[i]
#                 ll[i] = ll [i+1]
#                 ll[i+1] = temp
#     return list
#
# print(bsort(ll))

##############################################################################
# fibbonacci series
# def fibb(n):
#     return 0 if(n == 0) else(1 if (n==1 or n ==2) else (fibb(n-2) + fibb(n-1)))
#
# x = [fibb(x) for x in range(10)]
#
# print(x)
##############################################################################

# Palindrome:

# def palindrome(t):
#     return True if (t.lower() == t.lower()[::-1]) else False
#
# print(palindrome("Nitin"))

##############################################################################

# remove duplicates from list

# ll = "vishalv"
# k = list(ll)
# z = ll[::]
#
# def rl(l):
#     m = []
#     for x in l:
#         if l.count(x) > 1:
#             m.append(x)
#     return m
#
# print(set(rl(k)))
# print(set(z))

#####################################################################

# s = "Vishal is a Billionaire"
# l = s.split()
# print(len(l))

#####################################################################

s = "VISHAL03141994"

for c in s:
    if c.isdigit():
        print(c, end=" ")