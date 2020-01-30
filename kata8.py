# Another level 5 kata
"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

Example:
move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
"""
def move_zeros(array):
    zeroL = []
    finalL = []
    if len(array) > 0:
      for i in array:
        if i != None and i != [] and i != {} and i != () and type(i) != bool and type(i) != str:
          if int(i) == 0:
            zeroL.append(int(i))
          else:
            finalL.append(i)
        else:
          finalL.append(i)
      if len(zeroL) > 0:
        for z in zeroL:
          finalL.append(z)
    return finalL

print(move_zeros(["false",1,0,1,2,0,1,3,"a"]))
print(move_zeros([1,2,0,1,0,1,0,3,0,1]))
print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))
print(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]))
print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))
print(move_zeros([0,1,None,2,False,1,0]))
print(move_zeros(["a","b"]))
print(move_zeros(["a"]))
print(move_zeros([0,0]))
print(move_zeros([0]))
print(move_zeros([False]))
print(move_zeros([]))

# All tests passed at 100%. The code was also approved on Codewars

# Now other better solutions

# By riyakayal, Infi-chu, anDro!d, johnnybarrels, AnTmAn321, 万悠然
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

# By christopherj525, bevoy, percy22, Pixie11, yanitmagin, dacheng135 (plus 2 more warriors)

def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)


# By anter69, laos, bondario, domyos, user2811375, cth132 (plus 38 more warriors)
def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)
# This these last two only differ on the last condition. One is "bool" and the other is "False". It works the last one, but if there's "True", it fails.
# So the second one is more correct.

