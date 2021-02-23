def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True
#
# Write your code here.
#

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
