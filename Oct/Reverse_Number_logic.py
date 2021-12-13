# The Reverse Number Logic
# Take any number, reverse it and add it self
# do it until you will get one palindrome number

def is_palindrome(n):
    if n == int(str(n)[::-1]):
        return True

def reverse_num_logic(n):
    flag = True
    T = 0
    while flag:
        nr = int(str(n)[::-1])
        k = n + nr
        if len(str(k)) == 20:
            T = 0
            break
        if is_palindrome(k):
            flag=False
            T = k
            break
        n = k


    return T

for i in range(1,1000):
    z = reverse_num_logic(i)
    if z == 0:
        print(i)