# let's assume the user have two lists named Key and values
z = ['p', 'q', 'r', 's', 't']
y = [56, 67, 43, 12]
# the following method is used for comprehensiong the dictionary
user_Dict = { X:Y for (X,Y) in zip(z, y)}

print ("user_Dict: ", user_Dict)

merg = dict(zip(y,z))
print(merg)

sqr = {s:s**2 for s in range(1,10)}
print(sqr)

# list = [1, 2, 3, 4, 5, 6]
#
# z = (x ** 3 for x in list)
#
# print(next(z))
#
# print(next(z))
#
# print(next(z))
#
# print(next(z))
