/*
 From the previous Kata12. It works, but not good enough. It failed almost
 100 tests (in more than 300) on Codewars site.
   
   ++++++++++++++++++  Concatenation substring +++++++++++++++++++++

Write:

function findSubstring (s, words) {}

that given a string, "s", and a list of words, "words", that are all of the same length. Find all starting indices of substring in s that is a concatenation of each word in words exactly once and without any intervening characters.

*/

// Importing HasMap to be used
// import HashMap from '../hash-maps/hash-map';

/*
  Auxiliary class HashMap to deal with words storage and counting of words.

*/
class HashMap {
  constructor(initialCapacity = 2) {
    this.buckets = new Array(initialCapacity);
    this.collisions = 0;
  }

  set(key, value) {
    const bucketIndex = this.getIndex(key);
    if (this.buckets[bucketIndex]) {
      this.buckets[bucketIndex].push({ key, value });
      if (this.buckets[bucketIndex].length > 1) {
        this.collisions++;
      }
    } else {
      this.buckets[bucketIndex] = [{ key, value }];
    }
    return this;
  }

  get(key) {
    const bucketIndex = this.getIndex(key);
    for (
      let arrayIndex = 0;
      arrayIndex < this.buckets[bucketIndex].length;
      arrayIndex++
    ) {
      const entry = this.buckets[bucketIndex][arrayIndex];
      if (entry.key === key) {
        return entry.value;
      }
    }
  }

  hash(key) {
    let hashValue = 0;
    const stringTypeKey = `${key}${typeof key}`;

    for (let index = 0; index < stringTypeKey.length; index++) {
      const charCode = stringTypeKey.charCodeAt(index);
      hashValue += charCode << (index * 8);
    }

    return hashValue;
  }

  getIndex(key) {
    const indexHash = this.hash(key);
    const index = indexHash % this.buckets.length;
    return index;
  }
}

function findSubstring(s, words) {
  // Number of a characters of a word in array "words".
  var word_length = words[0].length;

  // Criation of a dictionary object to store the each word and its frequency
  firstDict = new Object();

  // Number of words present inside "words" array.
  var word_count = words.length;

  // Total characters present in "words" array.
  var wordsArraySize = word_length * word_count;

  // Resultant vector which stores indices.
  res = [];

  // If the total number of characters in "words" array
  // is more than length of string s itself.
  if (wordsArraySize > s.length) return res;

  // For each word from the "words" array, this one is copied in the dictionary.
  // If it's already there, its frequency is increased
  for (i = 0; i < word_count; i++) {
    if (firstDict[words[i]] !== undefined) firstDict[words[i]]++;
    else firstDict[words[i]] = 1;
  }

  // Using a temporary dictionary (as copy of the first one)
  // that will deal with each word frequency
  for (i = 0; i <= s.length - wordsArraySize; i++) {
    var tempDict = { ...firstDict };

    (j = i), (count = word_count);

    // Traversing the substring
    while (j < i + wordsArraySize) {
      // Extracting the word
      var word = s.substr(j, word_length);

      // If "word" is not found or if the frequency of current "word" is more than required, simply break.
      if (!(word in firstDict) || tempDict[word] == 0) break;
      // Otherwise decrement the count of "word" from the temporary dictionary
      else {
        tempDict[word]--;
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
