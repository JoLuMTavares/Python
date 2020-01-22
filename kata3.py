# importing the sys module 
import sys 

# Setting a recursion limit, so we can have a larger recursion limit
sys.setrecursionlimit(10**6) 

def reverse_seq(n):
  l = []
  if n > 0:
    l.append(n)
    l += reverse_seq(n-1)
  return l

# print(reverse_seq(10001))

# Sum of two arrays

# def array_plus_array(arr1,arr2):
#   return sum(i for i in arr1) + sum (j for j in arr2)
  

# print(array_plus_array([1,2,3], [8,9,10]))

# The Best solution from 
# GiacomoSorbi, lechevalier, EdgyEdgemond, Etoneja 
# in Codewars
array_plus_array=lambda a,b: sum(a+b)

# print(array_plus_array([1,2,3], [8,9,10]))

def orderL(prod, lst):
  finalList = [prod[0]]
  temp = [lst[0]]
  for i in range(1, len(lst)):
    if len(temp) == 1:
      if lst[i] > temp[0]:
        temp.insert(0, lst[i])
        finalList.insert(0, prod[i])
      else:
        temp.insert(i, lst[i])
        finalList.insert(i, prod[i])  
    else:
      for j in range(len(temp)-1):
        if lst[i] > temp[j]:
          temp.insert(j, lst[i])
          finalList.insert(j, prod[i])
          break
        elif lst[i] <= temp[j] and lst[i] > temp[j+1]:
          temp.insert(j+1, lst[i])
          finalList.insert(j+1, prod[i])
          break
        else:
          continue
      else:
        temp.append(lst[i])
        finalList.append(prod[i])
      
  return finalList


def multiply(a, pr):
  return [a[i] * pr[i] for i in range(len(a))]
  


def top3(products, amounts, prices):
  if len(products) > 0:
    if len(products) == 1:
      return products
    else:
      lst = multiply(amounts, prices)
      fLst = orderL(products, lst)
      return fLst[0:3]

# Other mutch better solutions

# By dolamroth
top3 = lambda x,y,z: [d[0] for d in sorted(list(zip(x,y,z)), key=lambda w: -w[1]*w[2])[:3]]

# By falsetru
import heapq

def top3(products, amounts, prices):
    items = zip(products, amounts, prices)
    return [product for product, _, _ in heapq.nlargest(3, items, key=lambda item: item[1] * item[2])]


# By theHawk85
def top3(*args):
    return [item[0] for item in sorted(zip(*args), key=lambda x: x[1]*x[2], reverse=True)[:3]]

# By CopperWye
import heapq
def top3(products, amounts, prices):
    return [tpl[0] for tpl in heapq.nlargest(3, zip(products, amounts, prices), key = lambda tpl: tpl[1] * tpl[2])] 

# print(top3(["Computer", "Cell Phones", "Vacuum Cleaner"], [3,24,8], [199,299,399]))

# print(top3(["Cell Phones", "Vacuum Cleaner", "Computer", "Autos", "Gold", "Fishing Rods", "Lego", " Speakers"], [5, 25, 2, 7, 10, 3, 2, 24], [51, 225, 22, 47, 510, 83, 82, 124]))

# print(top3(["Cell Phones", "Vacuum Cleaner", "Computer", "Autos", "Gold", "Fishing Rods", "Lego", " Speakers"], [0, 12, 24, 17, 19, 23, 120, 8], [9, 24, 29, 31, 51, 8, 120, 14]))


# ['Cell Phones', 'Vacuum Cleaner', 'Computer']
# ['Vacuum Cleaner', 'Gold', ' Speakers', 'Autos', 'Cell Phones', 'Fishing Rods', 'Lego', 'Computer']
# ['Lego', 'Gold', 'Computer', 'Autos', 'Vacuum Cleaner', 'Fishing Rods', ' Speakers', 'Cell Phones']