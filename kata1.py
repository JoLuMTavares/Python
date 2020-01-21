def duplicate_encode(word):
    for c in range(len(word)):
        for j in range(len(word)):
            if c != j and word[c].casefold() == word[j].casefold():
                print(")", end="")
                break
        else:
            print("(", end="")

duplicate_encode("(( @")
print()


# def getCount(inputStr):
#     num_vowels = 0
#     for s in inputStr:
#         if s in "aeiou":
#             num_vowels += 1
    
#     return num_vowels

# print(getCount("Checker"))


def getCount(s):
    return sum(c in 'aeiouAEIOU' for c in s)

print(getCount("Super Speed"))