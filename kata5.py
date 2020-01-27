"""
In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

Here's how it works:

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2

"""
# def digital_root(n):
#   if len(str(n)) == 1:
#     return n
#   else:
#     return digital_root(sum(int(digit) for digit in str(n)))

digital_root = lambda n: digital_root(sum(int(digit) for digit in str(n))) if len(str(n)) > 1 else n


print(digital_root(16))
print(digital_root(456))
print(digital_root(459))
print(digital_root(1234))
print()

# Another solution made by bartholomisha, user9000135, sandeep patel, Zhaow, 3rikthered, Fatcat560 (plus 11 more warriors)

# This works, but it's not recursive. 
def digital_root(n):
  return n%9 or n and 9 
# The goal is to make the solution in a recursive way.

print(digital_root(16))
print(digital_root(456))


# --------------------- MORSE CODE --------------------- #

# This kata is part of a series on the Morse code. After you solve this kata, you may move to the next one.

"""
In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superceded by voice and digital data communication channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−− ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

For example:

decodeMorse('.... . -.--   .--- ..- -.. .')
#should return "HEY JUDE"

NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

The Morse code table is preloaded for you as a dictionary, feel free to use it:

Coffeescript/C++/Go/JavaScript/Julia/PHP/Python/Ruby/TypeScript: MORSE_CODE['.--']
C#: MorseCode.Get(".--") (returns string)
Elixir: @morse_codes variable (from use MorseCode.Constants). Ignore the unused variable warning for morse_codes because it's no longer used and kept only for old solutions.
Elm: MorseCodes.get : Dict String String
Haskell: morseCodes ! ".--" (Codes are in a Map String String)
Java: MorseCode.get(".--")
Kotlin: MorseCode[".--"] ?: "" or MorseCode.getOrDefault(".--", "")
Rust: self.morse_code
Scala: morseCodes(".--")
C: provides parallel arrays, i.e. morse[2] == "-.-" for ascii[2] == "C"
All the test strings would contain valid Morse code, so you may skip checking for errors and exceptions. In C#, tests will fail if the solution code throws an exception, please keep that in mind. This is mostly because otherwise the engine would simply ignore the tests, resulting in a "valid" solution.

Good luck!

After you complete this kata, you may try yourself at Decode the Morse code, advanced.
"""
# MORSE_CODE['.--']

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'
}

# Decode implementation
# def decodeMorse(morse_code):
#     # ToDo: Accept dots, dashes and spaces, return human-readable message
#     return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')

def decodeMorse(morse_code):

    # Extra space for the end of this "morse_code" message
    morse_code += " "

    # Decipher that will store the final translater message
    decipher = ""

    # Cipher to store the morse code for one single character
    ciphtext = ""

    for mcc in morse_code:

      # Checking if there's a space in the message
      if mcc != " ":

        # A counter to track the number of spaces
        spaceC = 0

        # Storing one single character
        ciphtext += mcc

      else:
        
        # Incrementing the spaces counter
        spaceC += 1

        if spaceC == 3: # Then a new word is next
          decipher += " "

        elif spaceC < 2:
          # Accessing the keys of the dictionary by using their values 
          decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
                .values()).index(ciphtext)] 
          ciphtext = ''
    
    return decipher


print(MORSE_CODE['.--'])
print(decodeMorse('.... . -.--   .--- ..- -.. .'))