#############################################
# def isPrime(n):
#     for i in range(2,int(n**0.5)+1):
#       if (n%i == 0):
#         return False
#     else:
#       return True
#
# ll = []
# for i in range(100):
#   if isPrime(i):
#     ll.append(i)
#
# print(ll)
# print(len(ll))

print(ord("a"),chr(98))
n = 153
sum1 = [int(s)**(len(str(n))) for s in str(n)]
print(sum(sum1) == n)

import math

print(math.__dict__())