# def outer_div(func):
#     def inner(x,y):
#         if(x<y):
#             print("did changes")
#             x,y = y,x
#         return func(x,y)
#     return inner
#
# @outer_div
# def sub(x,y):
#     print(x - y)
#
#
# sub(2,5)


# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#
#     @property
#     def display(self):
#         return self.name + " got grade " + self.grade
#
#
# stu = Student("John", "B")
# print("Name:", stu.name)
# print("Grade:", stu.grade)
# print(stu.display)


# class Person:
#     @staticmethod
#     def hello():
#         print("Hello Peter")
#
#
# per = Person()
# per.hello()

def sm_div(func):
    def ddiv(a,b):
        if a<b:
            print("yo")
            a,b = b,a
        return func(a,b)
    return ddiv

@sm_div
def div(a,b):
    print(a/b)

div(2,4)