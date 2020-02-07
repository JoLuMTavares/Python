"""
Operator Insertion

An expression is formed by taking the digits 1 to 9 in numerical order and then inserting into each gap between the numbers either a plus sign or a minus sign or neither.

Your task is to write a method which takes one parameter and returns the smallest possible number of plus and minus signs necessary to form such an expression which equals the input.

Note: All digits from 1-9 must be used exactly once.

If there is no possible expression that evaluates to the input, then return null/nil/None.

There are 50 random tests with upper bound of the input = 1000.

Examples
When the input is 100, you need to return 3, since that is the minimum number of signs required, because: 123 - 45 - 67 + 89 = 100 (3 operators in total).

More examples:

 11  -->  5  #  1 + 2 + 34 + 56 + 7 - 89 = 11
100  -->  3  #  123 - 45 - 67 + 89 = 100
766  -->  4  #  1 - 2 + 34 - 56 + 789 = 766
160  -->  -  #  no solution possible

""" 
# 511 --> 4 # 1 - 2 + 34 + 567 - 89
# 515 --> 4 # 1 + 2 + 34 + 567 - 89
# 524 --> 3 # 12 + 34 + 567 - 89

# 711 --> 3 # 12 - 34 - 56 + 789
# 744 --> - #  no solution possible
# 770 --> 4 # 1 + 2 + 34 - 56 + 789
# 1073 --> 3  # 1234 - 5 - 67 - 89
# 1082 --> 3  # 1234 - 56 - 7 - 89
# 1083 --> 3  # 1234 + 5 - 67 - 89
# 1091 --> 3  # 1234 - 56 - 78 - 9
# 1096 --> 3  # 1234 - 56 + 7 - 89
# 1101 --> 3  # 1234 - 56 - 78 + 9

from itertools import product#, islice
 
# Auxiliary function that returns a complete string having all the digits
# Between each there can be an operator sign or not. 
def expr(p):
  return "1{}2{}3{}4{}5{}6{}7{}8{}9".format(*p)

 
# Auxiliary function that returns all the calculated expressions for each position
# between the 9 digits
def gen_expr():
  op = ['+', '-', '']
  return [expr(p) for p in product(op, repeat=9) if p[0] != '+']


# def all_exprs():
#   values = {}
#   for expr in gen_expr():
#       val = eval(expr)
#       if val not in values:
#           values[val] = 1
#       else:
#           values[val] += 1
#   return valuesf

# def sum_to(val):
#   for s in filter(lambda x: x[0] == val, map(lambda x: (eval(x), x), gen_expr())):
#       print(s)

# print(u"\u00B1")

# Auxiliary function that counts the number of operators inside the given string
def count_sign(e):
  count = 0
  for c in e:
    if ord(c) == 43 or ord(c) == 45:
      count += 1
  return count

count_oper = lambda e: sum(c  for c in str(e) if ord(c) == 43 or ord(c) == 45)

# This function gives the first right digit sequence before the final one
def make_expre(n):
  digits = "123456789"
  s_expr = str(n)
  if len(s_expr) > 1:
    first_expr = s_expr[0] + "".join(digits[digits.index(s_expr[0])+i] for i in range(1, len(s_expr)))
    return first_expr
  return None

def operator_insertor(n):
  # A list created with all the possible expressions that give result on the given
  # number
  l = list(filter(lambda x: x[0] == n, map(lambda x: (eval(x), x), gen_expr()))) 

  # Returning the count of the expression with the least operators inserted (when the list is not empty)
  return count_sign(l[len(l)-1][1]) if len(l) > 0 else None

print(make_expre(140))
print(make_expre(527))
print(make_expre(89))
print(make_expre(13))
print(make_expre(747))

print(operator_insertor(11))
print(operator_insertor(100))
print(operator_insertor(102))
print(operator_insertor(160))
print(operator_insertor(511))
print(operator_insertor(512))
print(operator_insertor(766))
print(operator_insertor(789))
print(operator_insertor(1091))


