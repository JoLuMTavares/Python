"""
############### Level 6 Kata ###############

## Transform To Prime ##

Task :
Given a List [] of n integers , find minimum mumber to be inserted in a list, so that sum of all elements of list should equal the closest prime number .

Notes
List size is at least 2 .

List's numbers will only positives (n > 0) .

Repeatition of numbers in the list could occur .

The newer list's sum should equal the closest prime number .

Input >> Output Examples

1- minimumNumber ({3,1,2}) ==> return (1)

Explanation:
Since , the sum of the list's elements equal to (6) , the minimum number to be inserted to transform the sum to prime number is (1) , which will make *the sum of the List** equal the closest prime number (7)* .

2-  minimumNumber ({2,12,8,4,6}) ==> return (5)

Explanation:
Since , the sum of the list's elements equal to (32) , the minimum number to be inserted to transform the sum to prime number is (5) , which will make *the sum of the List** equal the closest prime number (37)* .

3- minimumNumber ({50,39,49,6,17,28}) ==> return (2)

Explanation:
Since , the sum of the list's elements equal to (189) , the minimum number to be inserted to transform the sum to prime number is (2) , which will make *the sum of the List** equal the closest prime number (191)* .


"""

from math import sqrt
from itertools import count, islice

# Auxiliary function to get the sum of all elements in the list
sum_elem = lambda l: sum(e for e in l)

# Auxiliary function to check if a number is prime
# def isPrime(n):
#     if n < 2:
#         return False

#     for number in islice(count(2), int(sqrt(n) - 1)):
#         if n % number == 0:
#             return False

#     return True

# isPrime = lambda n: [False if n < 2 else False if n % number == 0 else True for number in islice(count(2), int(sqrt(n) - 1))][0]

# def minimum_number(numbers):
#   n = sum_elem(numbers)
#   min_n = 0
#   if isPrime(n):
#     return 0
#   while True:
#     min_n += 1
#     n += 1
#     if isPrime(n):
#       break
#   return min_n



# Another solution made by Blind4Basics

# def isPrime(n):
#     return n == 2 or n%2 and all(n%x for x in range(3,int(n**.5)+1,2))

# def minimum_number(numbers):
#     s = sum(numbers)
#     return next(x for x in count(0) if isPrime(s+x) )


# My lambda version after seeing the one above
# minimum_number = lambda numbers: next(x for x in count(0) if isPrime(sum(numbers)+x) )

# print(minimum_number([3,1,2]))
# print(minimum_number([5,2]))
# print(minimum_number([1,1,1]))
# print(minimum_number([2,12,8,4,6]))
# print(minimum_number([50,39,49,6,17,28]))

"""

############### Level 5 Kata ###############

Primes in numbers

Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

"(p1**n1)(p2**n2)...(pk**nk)"

with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"


"""

# Auxiliary function to check if a number is prime
isPrime = lambda n: n == 2 or n%2 and all(n%x for x in range(3,int(n**.5)+1,2))

def primeFactors(n):
  res = ""
  nList = []
  prevLen = len(nList)
  # First checking if the number is greater than 1
  if n > 1:
    
    # Performing the iteration. This will be until the multiplication of all the elements stored in the equals the given number    
    for e in range(2, n):

      # Checking if it is a prime number
      if isPrime(e):
        # Confirming if the given number is divisible by the prime one
        if n % e == 0:
          p = 2
          # If number is not divisible by the squared prime number
          if n % (e**p) != 0:
            nList.append(e) # Directly added to the list
            res += "(" + str(e) + ")" # A single string added
          else:
            p += 1
            # A cycle is performed until the given number is not divisible
            # by a specific power of the prime number
            while True:
              if n % (e**p) == 0:
                p += 1
              else:
                # Adding the limit. "p" must be the previous one, since it was
                # the last that worked
                nList.append(e**(p-1))

                # Adding the complete string with the right power 
                res += "(" + str(e) + "**" + str(p-1) + ")"
                break # Breaking the cycle

      # If the list is not empty and a new element was recently added to it
      if len(nList) > 0 and len(nList) > prevLen:
        prevLen += 1
        fN = 1

        # Getting the multiplication of all elements in this list
        for i in nList:
          fN *= i
        # If it matches the given number, we are done with cycles
        if fN == n:
          break
    if res != "":
      return res

  # In case nothing was done or we didn't get any possible sequence
  return "Empty. No sequence!"


# New version
def primeFactors_v2(n):
  # The string representing the sequence
  res = ""
  # The final number to compare to the given n
  fN = 1 
  # First checking if the number is greater than 1
  if n > 1:
    
    # Performing the iteration. This will be until the multiplication of all the elements stored in the equals the given number    
    for e in range(2, n):

      # Checking if it is a prime number
      if isPrime(e):
        # Confirming if the given number is divisible by the prime one
        if n % e == 0:
          p = 2
          
          # A cycle is performed until the given number is not divisible
          # by a specific power of the prime number
          while n % (e**p) == 0:
            p += 1
          else:
            # Multiplication of the main result by what is stored
            t = p-1
            fN *= e**(p-1)
            if t == 1:
              res += "(" + str(e) + ")"
            else:
              # Adding the complete string with the right power 
              res += "(" + str(e) + "**" + str(p-1) + ")"
            # break # Breaking the cycle

      # If it matches the given number, we are done with cycles
      if fN == n:
        break
    if res != "":
      return res

  # In case nothing was done or we didn't get any possible sequence
  return "Empty. No sequence!"

# print(primeFactors(121))
print(primeFactors(86240))
print(primeFactors(7775460)) # Correct. -> "(2**2)(3**3)(5)(7)(11**2)(17)"

print(primeFactors_v2(86240))
print(primeFactors_v2(7775460))
print(primeFactors_v2(27775460))
print(primeFactors_v2(18775465))
print(primeFactors_v2(208775469))
print(primeFactors_v2(198243782358748))
# print(primeFactors_v2(19824378235874820398457))
# The result is not entirely surprising. It works here.
# Not in code wars, since their servers are programmed not to go beyond 12 seconds
# of execution. This means, what I did is not efficient. I'll have to find
# another way if I want it to pass and to be much faster.