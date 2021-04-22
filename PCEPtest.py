# def fun(x,y):
#     if x == y:
#         return x;
#     else:
#         return fun(x,y-1)
#
# print(fun(0,3))

# my_tuple = ("v","i","s","h")
#
# my_tuple[1] = my_tuple[1] + my_tuple[0]
#
# print(my_tuple)


# my_list=[1,2]
#
# for v in range(2):
#     my_list.insert(-1,my_list[v])
#
# print(my_list)

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2
# print(fun(fun(2)))

# def fun(a , b, c=0):
#     return a + b + c
#
# print(fun(b=1, a=2))

# def func(a,b):
#     return b ** a
#
# print(func(b=2,2))


# tup=(1,2,4,8)
# tup = tup[-2:-1]
# print(tup)
# tup = tup[-1]
# print(tup)

# dct = {}
# dct['1'] = (1,2)
# dct['2'] = (2,1)
#
# for x in dct.keys():
#     print(dct[x][1],end="")

# lst = [[x for x in range(3)] for y in range(3)]
#
# for r in range (3):
#     for c in range(3):
#         if lst [r][c] % 2 != 0:
#             print("#")


# i = 0
# while i < i + 2:
#     i += 1
#     print("*")
# else:
#     print("*")

# print(1//2)

# lst =[i for i in range(-1,-2)]
# print(lst)

# my_list = [x * x for x in range (5)]
#
# def fun (lst):
#     del lst[lst[2]]
#     return lst
#
# print(my_list)
# print(fun(my_list))


# def fun(inp=2 , out=3):
#     return inp * out
#
# print(fun(out=2))

# dct = {"one":"two","three":"one","two":"three"}
# v = dct["three"]
#
# for k in range (len(dct)):
#     v = dct[v]
#
# print(v)

# def fun_1(a):
#     return None
#
# def fun_2(a):
#     return fun_1(a) * fun_1(a)
#
# print(fun_2(2))


# x =1
# y =2
# x,y,z = x,x,y
# z,y,z = x,y,z
#
# print(x,y,z)
#
# dd = {"1":"0","0":"1"}
# for x in dd.vals():
#     print(x, end="")

# num = [1,2,3]
# vals = num
# del vals[:]
#
# print(num)
# print(vals)


# z = 0
# y = 10
#
# x = y < z and z > y or y > z and z < y
# print(x)


# x = 1//5 + 1/5
# print(x)


# x = int(input())
# y = int(input())
#
# x = x % y
# x = x % y
# y = y % x
#
# print(y)

# x = float(input())
# y = float(input())
#
# print(y ** (1/x))
