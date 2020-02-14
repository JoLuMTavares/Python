// Class Binary Tree Node to be used on Binary Tree Class
// By ES2019, private class fields are declared by the use of -> #
// Visual Studio code is not yet updated with ES2019.
class BTNode {
  // ++ Three private elements ++
  // Node stored in the tree
  #element = '';

  // Left child of the node
  #leftChild = BTNode();

  // Right child of the node
  #rightChild = BTNode();

  // Constructor with a given element.
  // It initializes the one above with left and right children as null.
  constructor(theElement) {
    this(theElement, null, null);
  }

  // Constructor with a node, left and right child of the Binary tree
  constructor(theElement, leftE, rightE) {
    // Node stored in the tree
    this.#element = theElement;

    // Left child of the node
    this.#leftChild = leftE;

    // Right child of the node
    this.#rightChild = rightE;
  }

  // Returns the current node
  getElement() {
    return this.#element;
  }

  // Returns the left child
  getLeftChild() {
    return this.#leftChild;
  }

  // Returns the right child
  getRightChild() {
    return this.#rightChild;
  }

  // Setting a new node
  setElement(newElement) {
    this.#element = newElement;
  }

  // Setting a new leftChild
  setLeft(newLeft) {
    this.#leftChild = newLeft;
  }

  // Setting a new rightChild
  setRight(newRight) {
    this.#rightChild = newRight;
  }

  // Confirming that the current node has no children being, therefore, a leaf.
  isLeaf() {
    return this.#leftChild == null && this.#rightChild == null;
  }
}

// Class Binary Tree. This one is needed to be used on the main function
class BinaryTree extends BTNode {
  _root = new BTNode();
  currElem = '';

  // Returns true if the root of the tree is null. That is, no elements are in the tree.
  isEmpty() {
    return this._root == null;
  }

  // Prefix order. It calls another function bellow
  preorder() {
    this.preorder(this._root);
  }

  // Recursive prefix order. This is for searching a node.
  _preorder(node) {
    if (node !== null && node !== undefined) {
      this.currElem = node.getElement();
      this._preorder(node.getLeftChild());
      this._preorder(node.getRightChild());
    }
  }

  // Infix order. It calls another function bellow
  inorder() {
    this.inorder(this._root);
  }

  // Recursive Infix order. This is for searching a node.
  _inorder(node) {
    if (node !== null && node !== undefined) {
      this._inorder(node.getLeftChild());
      this.currElem = node.getElement();
      this._inorder(node.getRightChild());
    }
  }

  // Postix order. It calls another function bellow
  postorder() {
    this.postorder(this._root);
  }

  // Recursive postix order. This is for searching a node.
  _postorder(node) {
    if (node !== null && node !== undefined) {
      this._postorder(node.getLeftChild());
      this._postorder(node.getRightChild());
      this.currElem = node.getElement();
    }
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
