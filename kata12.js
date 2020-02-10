/*
  +++++++++   Level 5 Kata, only possible in Javascript +++++++++++
  ++++++++++++++++++  Concatenation substring +++++++++++++++++++++

Write:

function findSubstring (s, words) {}

that given a string, "s", and a list of words, "words", that are all of the same length. Find all starting indices of substring in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example:

findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]) === [6, 9, 12]
findSubstring("helloworld", ["world", "hello"]) === [0]
findSubstring("helloworld", ["bar", "foo"]) === []

*/

var findSubstring = (s, words) => {
  res = [];
  wordL = 0;
  countw = 0;
  seq = [];
  startIndex = 0;
  if (words.length > 0 && s.length > 0) {
    if (s.length >= 2 * words[0].length) {
      wordL = words[0].length;
      for (i = 0; i < s.length - words.length; i++) {
        for (j = i; j < s.length - words.length; j++) {
          currW = s.substr(s[j], s[j] + wordL - 1);
          if (words.includes(currW)) {
            if (!seq.includes(currW)) seq.push(currW);
            // else if (seq.length < words.length) seq.push(currW);
          }
          if (seq.length == words.length) {
            startIndex = s.indexOf(seq[0]);
            res.push(startIndex);
            seq = [];
            break;
          }
        }
      }
    }
  }
  return res;
};
