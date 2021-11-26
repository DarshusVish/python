
# n = int(input("enter"))
# k = False
# for i in range(2,n):
#     if (n%i == 0):
#         print("Is not prime")
#         k = False
#         break
#     else:
#         k = True
#
# if (k):
#     print("It is prime")
##########################################################################
# import time
# def prime_num_list(v,d):
#     for n in range(v,d):
#         k = True
#         for j in range(2,int(n**0.5)+1):
#             if (n%j == 0):
#                 # print("Is not prime")
#                 k = False
#                 break
#         if (k):
#             ll.append(n)
#
# v = int(input("Enter a number:- "))
# d = int(input("Enter a number:- "))
# ll = []
# start_time = time.time()
# prime_num_list(v,d)
# end_time = time.time()
# total = end_time - start_time
# print(ll)
# print(len(ll))
# print(total)
# [0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
####################################################################

# An = []
# for i in range(1,100000):
#     n = i
#     b=len(str(n))
#     sum1 = [int(s)**b for s in str(n)]
#     if(sum(sum1) == n ):
#         An.append(n)
#
# print(An)
######################################################################


# ll = ("vishal")
# l2 = []
# c = len(ll)
# for i in range(c):
#     l2.append(ll[(c-1)-i])
# 
# print("".join(l2))

########################################################

# n = 153
# sum1 = [ int(i)**3 for i in str(n)]
# print(sum(sum1) == n)

########################################################

# n = 57
# k = False
# for i in range(2,n):
#     if (n%i == 0):
#         print("it is not prime")
#         k = False
#         break
#     else:
#         k = True
#
# if (k):
#     print("It is prime")



########################################################
def prime_num(v,d):
    for n in range(v,d):
        k = True
        for j in range(2,n):
            if (n%j == 0):
                k = False
                break
            else:
                k = True
        if k:
            ll.append(n)

ll = []
prime_num(1,10)
print(ll)