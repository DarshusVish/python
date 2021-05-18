str1= input("Please enter a string:- ").lower()
vowels = "aeiou"
v_count = 0
c_count = 0
list_v =[]
for i in str1:
    if i in vowels and i.isalpha():
        v_count += 1
    elif i.isalpha() :
        c_count +=1

print(v_count)
print(c_count)
