# ++++++++++++++++++ Level 5 Kata (When I'm ranked level 7) ++++++++++ #
"""

Consider the sequence U(n, x) = x + 2x**2 + 3x**3 + .. + nx**n where x is a real number and n a positive integer.

When n goes to infinity and x has a correct value (ie x is in its domain of convergence D), U(n, x) goes to a finite limit m depending on x.

Usually given x we try to find m. Here we will try to find x (x real, 0 < x < 1) when m is given (m real, m > 0).

Let us call solve the function solve(m) which returns x such as U(n, x) goes to m when n goes to infinity.

Examples:
solve(2.0) returns 0.5 since U(n, 0.5) goes to 2 when n goes to infinity.

solve(8.0) returns 0.7034648345913732 since U(n, 0.7034648345913732) goes to 8 when n goes to infinity.

Note:
You pass the tests if abs(actual - expected) <= 1e-12

"""

# def U(n, x):
#   return (nx^(n+2) - (n+1)x^(n+1) + x)/(1-x)

  # (1-x)m = nx^(n+2) - (n+1)x^(n+1) + x

  # x(1-x)m = n^(n+2) - (n+1)^(n+1) + 1

  # x(1-x) = (n^(n+2) - (n+1)^(n+1) + 1) / m


def solve(m):
  pass


##################### NEXT ONE ++++++++++++++++++++++++++++++++++++++
"""
The number 81 has a special property, a certain power of the sum of its digits is equal to 81 (nine squared). Eighty one (81), is the first number in having this property (not considering numbers of one digit). The next one, is 512. Let's see both cases with the details

8 + 1 = 9 and 9² = 81

512 = 5 + 1 + 2 = 8 and 8³ = 512

We need to make a function, power_sumDigTerm(), that receives a number n and may output the n-th term of this sequence of numbers. The cases we presented above means that

power_sumDigTerm(1) == 81

power_sumDigTerm(2) == 512

Happy coding!

"""

# Auxiliary function to sum the digits of a number
digit_sum = lambda n: sum(int(digit) for digit in str(n))

digital_root = lambda n: digital_root(sum(int(digit) for digit in str(n))) if len(str(n)) > 1 else n

def power_sumDigTerm(n):
  p = 0
  for i in range(2, 10):
    p = i**(n+1)
    if digit_sum(p) == i:
      break
  return p
    # return x # n-th term of the sequence, each term is a power of the sum of its digits


# power_sumDigTerm_L: lambda n: p if digit_sum(p) == i for i in range(2, 10) and p = i**(n+1)

power_sumDigTerm_List = lambda n: list(map(lambda i: i**(n+1) , [i for i in range(2, 10) if digit_sum(i**(n+1)) == i]))[0]

"""
Both solutions are not good. I had a bad interpretation.
The given n is not a sequence. It's really to find the n-th term.

A found example:


from math import *  # because math should never be in a module

def digitSum(n):
    return sum(int(x) for x in str(n))

def isPowerOf(a,b):
    # using log WILL FAIL due to floating-point errors
    # e.g. log_3{5832} = 3.0000..04
    if b<=1:
        return False
    # using http://stackoverflow.com/a/4429063/711085
    while a%b==0:
        a = a / b
    return a==1

def test(n):
    return isPowerOf(n, digitSum(n))

M = 723019613391360  # max number to check
candidates = set(n**m for n in range(int(sqrt(M)+1)) 
                       for m in range(int(log(M,max(n,2)))+1))
result = list(sorted([c for c in candidates if test(c)]))

This solution probably works. The problem is, it takes several minutes.
It won't do it at all.

Another one next:


import heapq
import functools

def get_powers():
    heap = []
    push = functools.partial(heapq.heappush, heap)
    pop = functools.partial(heapq.heappop, heap)
    nextbase = 3
    nextbasesquared = nextbase ** 2
    push((2**2, 2, 2))
    while 1:
        value, base, power = pop()
        if base % 9 == value % 9:
            r = 0
            n = value
            while n:
                r, n = r + n % 10, n // 10
            if r == base:
                yield value, base, power
        power += 1
        value *= base
        push((value, base, power))
        if value > nextbasesquared:
            push((nextbasesquared, nextbase, 2))
            nextbase += 1
            nextbasesquared = nextbase ** 2


for i, info in enumerate(get_powers(), 1):
    print(i, info)

This solution is quite reasonable until it reaches the 28th time to get
the right "power". Then it gets slower and slower.

Another one:


import cProfile

import math

MAXNUM = 10000000

powersOf10 = [10 ** n for n in range(0, int(math.log10(MAXNUM)))]

print(powersOf10)

def powerOfSum1():
    listOfN = []
    arange = range(11, MAXNUM) #range of potential Ns
    prange = range(2, 6) # a range for the powers to calculate
    for num in arange:
        sumOfDigits = 0
        for p in powersOf10:
            sumOfDigits += num / p % 10
        powersOfSum = []
        curr = sumOfDigits
        for p in prange:
            curr = curr * sumOfDigits
            if num < curr:
                break
            if num == curr:
                listOfN.append(num)
    return listOfN

This solution is not reasonable. It has real numbers. It makes no sense to compare
a float to an integer. That never gives True. Using any arithmetic operator to get
an integer is also not good (since it may come out an integer plus or one, for example).

To make it worse, in the end, the list is exactly empty. And it wasn't much faster
either like the author of this mentioned.

This has nothing to do with profiler. The profiler is important. The problem here is, this code has no logic to get even one single correct value, unlike the previous one where we see the results (even if it gets really slow).

One more here:

"""

def powerOfSum():
    listOfN = []
    for base in range(2, 100):
        num = base
        for _ in range(2, 10):
            num *= base
            if sum(map(int, str(num))) == base:
                listOfN.append(num)
    return sorted(listOfN)[:30]

print(powerOfSum()) # It works really fast indeed. But it only gets up to 33.

# Some adaptation

def powerOfSum_Term(n):
    listOfN = []
    for base in range(2, 500): # Increased so it makes more calculations
        num = base
        for _ in range(2, 30): # Increased for a larger power range
            num *= base
            if digit_sum(num) == base:  # My version of digit_sum
                listOfN.append(num)
    sortedL = sorted(listOfN)
    return sortedL[n-1]

print("Newest vertion.")
print(powerOfSum_Term(1))
print(powerOfSum_Term(2))
print(powerOfSum_Term(3))
print(powerOfSum_Term(4))
print(powerOfSum_Term(5))
print(powerOfSum_Term(6))
print(powerOfSum_Term(7))
print(powerOfSum_Term(37))
# This is the version that passed there.

print()
print("First version - ")
print(power_sumDigTerm(1))
print(power_sumDigTerm(2))
print(power_sumDigTerm(3))
print(power_sumDigTerm(4))

print()
# print("A list with powers...")
# print(powerOfSum1())

# print()
# print("With list maps.")
# print(power_sumDigTerm_List(1))
# print(power_sumDigTerm_List(2))
# print(power_sumDigTerm_List(3))
# print(power_sumDigTerm_List(4))

# Now some solutions made by others. There's a great one.

# By CrazyMerlyn
def dig_sum(n):
    return sum(map(int, str(n)))

terms = []
for b in range(2, 400):
    for p in range(2, 50):
        if dig_sum(b ** p) == b:
            terms.append(b ** p)
terms.sort()

def power_sumDigTerm(n):
    return terms[n - 1]
# A litle bit similar as mine

# By anter69
power_sumDigTerm = [None, 81, 512, 2401, 4913, 5832, 17576, 19683, 234256,
    390625, 614656, 1679616, 17210368, 34012224, 52521875, 60466176, 205962976,
    612220032, 8303765625, 10460353203, 24794911296, 27512614111, 52523350144,
    68719476736, 271818611107, 1174711139837, 2207984167552, 6722988818432,
    20047612231936, 72301961339136, 248155780267521, 3904305912313344,
    45848500718449031, 81920000000000000, 150094635296999121, 13744803133596058624,
    19687440434072265625, 53861511409489970176, 73742412689492826049,
    179084769654285362176, 480682838924478847449].__getitem__
# The classical cheating or assuming way. Of course it works, except when it comes
# a term out of the range    


# By VovaK
def power_sumDigTerm_V(n):
    return sorted([i**j for j in range(2,50) for i in range(2,100) if i == sum([int(i) for i in str(i**j) ])])[n-1]
print("Made by Vovak. In case of the 38th-term - ", power_sumDigTerm_V(38))

# This is professional programming. Tested and it works well.


