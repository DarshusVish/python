# def simple():
#     for i in range(10):
#         if (i % 2 == 0):
#             yield i
#
#         # Successive Function call using for loop
# for i in simple():
#     print(i)

##############################################################

def multiple_yield():
    str1 = "First String"
    yield str1

    str2 = "Second string"
    yield str2

    str3 = "Third String"
    yield str3


obj = multiple_yield()
print(next(obj))
print(next(obj))
print(next(obj))