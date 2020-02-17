/*
 From the previous Kata12. It works, but not good enough. It failed almost
 100 tests (in more than 300) on Codewars site.
   
   ++++++++++++++++++  Concatenation substring +++++++++++++++++++++

Write:

function findSubstring (s, words) {}

that given a string, "s", and a list of words, "words", that are all of the same length. Find all starting indices of substring in s that is a concatenation of each word in words exactly once and without any intervening characters.

*/

function findSubstring(s, words) {
  // Number of a characters of a word in array "words".
  var word_length = words[0].length;

  // Criation of a dictionary object to store the each word and its frequency
  firstDict = new Object();

  // Map which comes included on ES6
  firstHash = new Map();

  // Number of words present inside "words" array.
  var word_count = words.length;

  // Total characters present in "words" array.
  var wordsArraySize = word_length * word_count;

  // Resultant vector which stores indices.
  res = [];

  // If the total number of characters in "words" array
  // is more than length of string s itself.
  if (wordsArraySize > s.length) return res;

  // For each word from the "words" array, this one is inserted in the Map.
  // If it's already there, its frequency (value) is increased
  for (i = 0; i < word_count; i++) {
    if (firstHash.has(words[i])) {
      val = firstHash.get(words[i]);
      firstHash.set(words[i], ++val);
    } else firstHash.set(words[i], 1);
  }
  // Using a temporary Map (as copy of the first one)
  // that will deal with each word frequency
  for (i = 0; i <= s.length - wordsArraySize; i++) {
    var tempHash = new Map(firstHash);

    (j = i), (count = word_count);

    // Traversing the substring
    while (j < i + wordsArraySize) {
      // Extracting the word
      var word = s.substr(j, word_length);

      // If "word" is not found or if the frequency of current "word" is more than required, simply break.
      if (
        !firstHash.has(word) ||
        (tempHash.get(word) !== undefined && tempHash.get(word) == 0)
      )
        break;
      // Otherwise decrement the count of "word" from the temporary Map
      else {
        tempVal = tempHash.get(word);
        tempHash.set(word, --tempVal);
        count--;
      }

      j += word_length;
    }
    // Store the starting index of that substring when all the words in the list are in substring
    if (count == 0) res.push(i);
  }
  // Returning the result
  return res;
}

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
