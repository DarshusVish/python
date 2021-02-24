# def fun1(a):
#     return None
#
# def fun2(a):
#     return fun1(a) * fun1(a)
#
# print(fun2(2))

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2
#
# print(fun(fun(2)))

# z = 0
# y = 10
# x = y < z and z > y or y > z and z < y
# print(x)

# def fun(x ,y):
# #     if x == y:
# #         return x
# #     else:
# #         return fun(x, y-1)
# #
# # print(fun(0,3))

# x = float(input())
# y = float(input())
# print(y ** (1/x))


# lst=[i for i in range(-1,-2)]
# print(lst)

# dct = {}
# dct['1'] = (1,2)
# dct['2'] = (2,1)
#
# for x in dct.keys():
#     print(dct[x][1], end="")

# myl = [1,2]
#
# for v in range(2):
#     myl.insert(-1, myl[v])
#
# print(myl)

# dct = {'one':'two', 'three':'one','two':'three'}
# v = dct['three']
#
# for k in range(len(dct)):
#     v = dct[v]
#
# print(v)

# dd = {"1":"0","0":"1"}
# for x in dd.vals():
#     print(x, end="")

# myl = [ x * x for x in range(5)]
#
# def fun(lst):
#     del lst[lst[2]]
#     return lst
# print(fun(myl))


# x = 1
# y = 2
# x,y,z = x,x,y
# z,y,z = x,y,z
#
# print(x,y,z)

# y = input()
# # # x = input()
# # # print(x + y)

# def fun(a,b):
#     return b ** a
#
# print(fun(b=2, 2))

# x = 1 // 5 + 1/5
# print(x)


# a =1
# b=0
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print(a,b)

# num = [1,2,3]
# val = num
# del val[:]
#
# print(num)
# print(val)


# x = 1 //2
# print(x)

# x = int(input())
# y = int(input())
#
# x = x % y
# x = x % y
# y = y % x
#
# print(y)

# def fun(a, b,c=0):
#     print(a,b,c)
#
# fun(b=0,a=0)

# i = 0
# while i < i +2:
#     i += 1
#     print("*")
# else:
#     print("*")

# tup = (1,2,4,8)
# tup = tup[-2:-1]
# tup= tup[-1]
# print(tup)

# lst = [[x for x in range(3)] for y in range(3)]
#
# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 != 0:
#             print("#")
