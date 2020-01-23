def divisors(n):
  c = 1
  for i in range(1, n):
    if n % i == 0:
      c += 1
  return c

# print(divisors(16))

# Another version

divisors = lambda n: sum(n % c == 0 for c in range(1, n+2))
print(divisors(4096))

# Other solutions
# By ssobczak, jolaf, sfr

def divisors(n):
    return sum(1 for i in xrange(1, n + 1) if n % i == 0)

# By polyglotm. 
# 
# He made 5 different versions. The last one is like mine, only he uses a list # while I'm dealing with direct boolean True values counting.


# For Beginners.

# Time: 11724ms
# it's slow because use isinstance
def divisors5(n):
    return len(list(filter(lambda e: isinstance(e, int), [x if n % x == 0 else None for x in range(1, n + 1)])))


# Time: 7546ms
# it's little fast because just directly check boolean
def divisors4(n):
    return len(list(filter(lambda e: e, [True if n % x == 0 else False for x in range(1, n + 1)])))


# Time: 4731ms
# in python True is evaluate as 1
# so when prime factorization just set True and sum will return count
def divisors3(n):
    return sum([True if n % x == 0 else False for x in range(1, n + 1)])


# Time: 3675ms
# even don't need return true, cause comparison operator will return boolean
def divisors2(n):
    return sum([n % x == 0 for x in range(1, n + 1)])


# same time with above but make short code via lambda expression
divisors = lambda n: sum([n % x == 0 for x in range(1, n + 1)])

# ++++++++++++++++++++++++++++++ ///////// ++++++++++++++++++++++++++++++

"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt" 

"""
# def accum(s):
#   fs = ""
#   for c in range(1, len(s)):
#     fs += (c*s[c-1] + "-").capitalize()
#   else:
#     fs += ((c+1)*s[c]).capitalize()
#   return fs
# This was the one submitted

# def accum(s):
#   print([(c*s[c-1]).capitalize()] for c in range(1, len(s)+1), sep="-"

accum = lambda s: "-".join((c*s[c-1]).capitalize() for c in range(1, len(s)+1))
# I only got this one after seeing how the others in Codewars did their solutions.

print(accum("abcd"))
print(accum("RqaEzty"))
print(accum("cwAt"))

# Other solutions
# By colbydauph, GNX, ecolban, user349500, biskinis, LawlietRyuzaki69 (plus 163 more warriors)

# def accum(s):
#     return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

# # By zebulan, Kalinin308, Srinandu, xihuishaw, l2961684, D0588559 (plus 12 more warriors)

# def accum(s):
#     return '-'.join((a * i).title() for i, a in enumerate(s, 1))
