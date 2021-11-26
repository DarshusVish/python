myPrimeNumbers = []
i = 1
while i <= 10:

  if i > 1:
    isPrime = True
  else:
    isPrime = False

  j = 2
  while j < i:
    if i%j == 0:
      isPrime = False
      break
    j += 1

  if isPrime:
    # print(i, "is a prime number")
    myPrimeNumbers.append(i)

  i += 1

print(myPrimeNumbers)