"""
def longest(a, b):
  s1 = []
  if a != "":
    if len(a) == 1:
      s1.append(a)
    else:
      for i in range(len(a)):
        if a[i] in s1:
          pass
        else:
          s1 += a[i]
      
  if b != "":
    if len(b) == 1:
      s1 += b
    else:
      for j in range(len(b)):
        if b[j] in s1:
          pass
        else:
          s1 += b[j]
  fs1 = ""
  
  for c in sorted(s1):
    fs1 += c
  
  return fs1
  

a = "oaijfhufisjfisdifj"
b = "aoskdjaidsjfiiieuzrfusufzsdfhsdufhbds"

print(longest(a, b))
"""

def insertElem(s, fs):
  for i in range(len(s)):
    if s[i] not in fs:
      fs += s[i]
  return fs

def longest(a, b):
  s1 = []
  if a != "":
    if len(a) == 1:
      s1.append(a)
    else:
      s1 = insertElem(a, s1)

  if b != "":
    if len(b) == 1:
      s1 += b
    else:
      s1 = insertElem(b, s1)
  fs1 = ""
  
  for c in sorted(s1):
    fs1 += c
  
  return fs1
  

a = "oaijfhufisjfisdifj"
b = "aoskdjaidsjfiiieuzrfusufzsdfhsdufhbds"

# print(longest(a, b))

# A very direct version (from Codewars)
def longest(s1, s2):
    return ''.join(sorted((set(s1+s2))))

a = "oaijfhufisjfisdifj"
b = "aoskdjaidsjfiiieuzrfusufzsdfhsdufhbds"

print(longest(a, b))