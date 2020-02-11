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

// Auxiliary function to count the number of repetitions of an item in an array.
// Basically, it's like giving the number of duplicates.
function checkDuplicates(theArray) {
  var object = {}; // Temporary object
  var result = 0; // The counter

  // If the temporary object doesn't have the item, it inserts with the value 0.
  // Otherwise it increases the value by 1.
  theArray.forEach(function(item) {
    if (!object[item]) object[item] = 0;
    object[item] += 1;
  });

  // For each item stored (as key) in the object, we get the associated value.
  for (var prop in object) {
    if (object[prop] >= 2) {
      result += object[prop] - 1; // Always minus 1. Thats the number of repetitions.
    }
  }

  return result;
}

var findSubstring = (s, words) => {
  res = [];
  wordL = 0;
  countw = 0;
  currW = '';
  seq = [];
  startIndex = 0;

  // Checking first if both elements are not empty
  if (words.length > 0 && s.length > 0) {
    rep = checkDuplicates(words);
    // Checking if the length of the string is at least the same as of all the words
    // in the array concatenated
    if (s.length >= words.length * words[0].length) {
      wordL = words[0].length;
      // The main sequence, character by character. Important that when the length of "the ///  remaining characters to be checked" is less than the all the "words" concatenated,
      // we stop, since there's no point on keep going.
      for (i = 0; i < s.length - words.length * wordL + 1; i++) {
        startIndex = i; // The start index
        duplic = rep; // When there are repetitions
        // Checking for all the elements stored in the array and cheking if the
        // sequence in the string is a perfect match and there are no different
        // characters
        for (j = 0; j < words.length; j++) {
          // It is always word by word in this case
          currW = s.substr(i + j * wordL, wordL);
          if (words.includes(currW)) {
            if (!seq.includes(currW)) {
              seq.push(currW);
              currW = '';
            } else if (duplic > 0) {
              // If the are duplicates, then it still counts
              seq.push(currW);
              currW = '';
              // Decreasing so this also stops when it reaches 0.
              duplic--;
            } else {
              seq = [];
              break;
            }
          } else break; // No matches, we move to the next character

          // When the sequence length has the same length has the "words" array, we have
          // completed the cycle of words and the sequence match.
          if (seq.length == words.length) {
            res.push(startIndex); // Store the starting index.
            seq = [];
            break;
          }
        }
        if (seq.length > 0) seq = []; // Resetting for a new cycle.
      }
    }
  }
  return res;
};

console.log(findSubstring('barfoofoobarthefoobarman', ['bar', 'foo', 'the']));
console.log(findSubstring('helloworld', ['world', 'hello']));
console.log(
  findSubstring('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'good'])
);
console.log(findSubstring('helloworld', ['bar', 'foo']));
console.log(
  findSubstring('lingmindraboofooowingdingbarrwingmonkeypoundcake', [
    'fooo',
    'barr',
    'wing',
    'ding',
    'wing'
  ])
);
console.log(findSubstring('aaaaaaaa', ['aa', 'aa', 'aa']));
