"""
##############  Sequence of Power Digits Sum  ##############

Let's take an integer number, start and let's do the iterative process described below:

we take its digits and raise each of them to a certain power, n, and add all those values up. (result = r1)

we repeat the same process with the value r1 and so on, k times.

Let's do it with start = 420, n = 3, k = 5:

420 ---> 72 (= 4³ + 2³ + 0³) ---> 351 (= 7³ + 2³) ---> 153 ---> 153 ----> 153


We can observe that it took 3 steps to reach a cyclical pattern [153](h = 3). The length of this cyclical pattern is 1, patt_len. The last term of our k operations is 153, last_term

Now, start = 420, n = 4, k = 30:

420 ---> 272 ---> 2433 ---> 434 ---> 593 ---> 7267 --->
6114 ---> 1554 ---> 1507 ---> 3027 ---> 2498 ---> 10929 --->
13139 ---> 6725 ---> 4338 ---> 4514 ---> 1138 ---> 4179 ---> 9219 ---> 
13139 ---> 6725 ---> 4338 ---> 4514 ---> 1138 ---> 4179 ---> 9219 ---> 
13139 ---> 6725 ---> 4338 ---> 4514 ---> 1138 ---> 4179 ---> 9219......

In this example we can observe that the cyclical pattern (cyc_patt_arr) is [13139, 6725, 4338, 4514, 1138, 4179, 9219] with a length of 7, (patt_len = 7), and it took 12 steps (h = 12) to reach the cyclical pattern. The last term after doing 30 operations is 1138

Make the function sum_pow_dig_seq(), that receives the arguments in the order shown below with the corresponding output:

sum_pow_dig_seq(start, n, k) ---> [h, cyc_patt_arr, patt_len, last_term]


For our given examples,

sum_pow_dig_seq(420, 3, 5) == [3, [153], 1, 153]

sum_pow_dig_seq(420, 4, 30) == [12, [13139, 6725, 4338, 4514, 1138, 4179, 9219], 7, 1138]

500 ≤ start ≤ 8000
2 ≤ n ≤ 9
100 * n ≤ k ≤ 200 * n

"""


# Auxiliary function to get the sum of the n power of each digit
digit_power_sum = lambda b, n: sum(int(digit)**n for digit in str(b))

def sum_pow_dig_seq(start, n, k):
    h = 0
    cyc_patt_arr = []
    patt_len = 0
    last_term = 0
    complete_patt = []
    for i in range(k):
      if len(complete_patt) == 0:
        v = digit_power_sum(start, n)
        complete_patt.append(v)
      else:
        v = digit_power_sum(complete_patt[len(complete_patt)-1], n)
        complete_patt.append(v)
    # compl_pt = []
    # compl_pt = list(map(lambda i: digit_power_sum(start, n) if len(compl_pt) == 0 else digit_power_sum(compl_pt[len(compl_pt)-1], n), [i for i in range(k)]))
    # print(compl_pt)
    # print(complete_patt)
    seq = []
    if len(complete_patt) > 0:
      for e in range(len(complete_patt)):
          if complete_patt[e] in seq:
            h = seq.index(complete_patt[e]) + 1
            cyc_patt_arr = list(map(lambda i: seq[i], [i for i in range(h-1, len(seq))]))
            patt_len = len(cyc_patt_arr)
            last_term = complete_patt[len(complete_patt)-1]
            break
          else:
            seq.append(complete_patt[e])



    return [h, cyc_patt_arr, patt_len, last_term]


print(sum_pow_dig_seq(420, 3, 5))
print(sum_pow_dig_seq(420, 4, 30))
print(sum_pow_dig_seq(420, 5, 100))


# Another solution made by anter69

def sum_pow_dig_seq(num, exp, k):
    seq = []
    
    for step in range(k):
        seq.append(num)
        num = sum( int(dig) ** exp for dig in str(num) )
        
        if num in seq:
            cycle_start = seq.index(num)
            cycle = seq[cycle_start:]
            last_term = cycle[(k - cycle_start) % len(cycle)]
            return [ cycle_start, cycle, len(cycle), last_term ]
    
    return [ 0, [], 0, num ]

