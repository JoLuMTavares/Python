# import unittest
"""
Polycarpus works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance. Recently, he has decided to take a couple of old songs and make dubstep remixes from them.

Let's assume that a song consists of some number of words (that don't contain WUB). To make the dubstep remix of this song, Polycarpus inserts a certain number of words "WUB" before the first word of the song (the number may be zero), after the last word (the number may be zero), and between words (at least one between any pair of neighbouring words), and then the boy glues together all the words, including "WUB", in one string and plays the song at the club.

For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX".

Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, he decided to find out what was the initial song that Polycarpus remixed. Help Jonny restore the original song.

Input
The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters

Output
Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.

Examples

song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND
"""

def song_decoder(song):
    if len(song) <= 200:
      original = "" # The final string and original song name
      countsq = 0 # Counter for when there's more than one "WUB" sequence
      i = 0
      while i < len(song):
        if song[i] == "W" and song[i+1] == "U" and song[i+2] == "B":
          if countsq == 0:
            original += " "
            i += 3
            countsq += 1
          else: # If the counter is greater than 0, no more spaces are added
            i += 3
            countsq += 1
        else:
          original += song[i]
          i += 1
          if countsq > 0:
              countsq = 0 # Resetting the counter
    return original.strip()

# --------------------------------- /// --------------------------------- #
# Other much better solutions

# ---------------------------------

# By isbadawi, richlewis42, chriscannon, 9394974, jselsing, jabbson (plus 1388 more warriors)

# def song_decoder(song):
#     return " ".join(song.replace('WUB', ' ').split())

# ---------------------------------

# By rmobis, bbm, staticor, kavag, js572, vnjogani (plus 486 more warriors)

# def song_decoder(song):
#     import re
#     return re.sub('(WUB)+', ' ', song).strip()

# ---------------------------------

# By pavel.koshev, Kironide, woj_swiderski, Akawak23, GreyD3204, Som Nek

# def song_decoder(song):
#     return ' '.join([a for a in song.split('WUB') if a])

# --------------------------------- \\\ --------------------------------- #

# After analysing their solutions, here my final one

song_decoder_L = lambda song: " ".join(song.replace("WUB", " ").split())

print(song_decoder_L("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
print(song_decoder("AWUBWUBWUBBWUBWUBWUBC")) # First (many code lines) version
print(song_decoder_L("WUBAWUBBWUBCWUB"))

# Test.assert_equals(song_decoder("AWUBBWUBC"), "A B C","WUB should be replaced by 1 space")
# Test.assert_equals(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C","multiples WUB should be replaced by only 1 space")
# Test.assert_equals(song_decoder("WUBAWUBBWUBCWUB"), "A B C","heading or trailing spaces should be removed")
print()
print(40*"+")
print()

# --------------------------------- ++++ --------------------------------- #

"""
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.

Examples:

tickets([25, 25, 50]) # => YES 
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)

"""

def tickets(people):
    if len(people) > 0:
      deposit = 0
      for bill in people:
        if bill == 25:
          deposit += bill
        else:
          deposit -= (bill -25)
      if deposit >= 0:
        return "YES"
      else:
        return "NO"

# tickets = lambda people: "NO" for bill in people if bill > 25 and (if (change = bill -25) > deposit) else "YES" else deposit += bill

print(tickets([25, 25, 50]))
print(tickets([25, 100]))
print(tickets([25, 25, 50, 50, 100]))
print(tickets([25, 25, 50, 50, 25, 25, 25, 100, 25, 50]))

# This exercise also has some issues as those were reported by other programmers
# already.