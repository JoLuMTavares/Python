"""
  ++++++++++++++++ Back to Python ++++++++++++++++

  **************** Binary Tree. This time it's the main exercise.

  Definition: According to Wikipedia, a complete binary tree is a binary tree "where every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible."

The Wikipedia page referenced above also mentions that "Binary trees can also be stored in breadth-first order as an implicit data structure in arrays, and if the tree is a complete binary tree, this method wastes no space."

Your task is to write a method (or function) that takes an array (or list, depending on language) of integers and, assuming that the array is ordered according to an in-order traversal of a complete binary tree, returns an array that contains the values of the tree in breadth-first order.

Example 1: Let the input array be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. This array contains the values of the following complete binary tree.

                          _7_
                        /     \
                       4       9
                     /   \    / \
                    3     6  8   10
                   / \    /
                  1   2  5 

  In this example, the input array happens to be sorted, but that is not a requirement.

Output 1: The output of the function shall be an array containing the values of the nodes of the binary tree read top-to-bottom, left-to-right. In this example, the returned array should be:

[7, 4, 9, 2, 6, 8, 10, 1, 3, 5]

Example 2: Let the input array be [1, 2, 2, 6, 7, 5]. This array contains the values of the following complete binary tree.

                          6
                        /   \
                       2     5
                      / \    /
                     1   2  7

Note that an in-order traversal of this tree produces the input array.

Output 2: The output of the function shall be an array containing the values of the nodes of the binary tree read top-to-bottom, left-to-right. In this example, the returned array should be:

[6, 2, 5, 1, 2, 7]

"""

# Class BTNode that represents a each node of a tree

class BTNode:

  # Constructor of the binary tree  
  def __init__(self, theElement, leftNode=None, rightNode=None):
    __self.leftChild = leftNode
    __self.rightChild = rightNode
    __self.element = theElement


  # Getting the current node
  def getElement(self):
    return __self.element

  # Getting the left child of the node
  def getLeft(self):
    return __self.leftChild

  # Getting the right child of the node
  def getRight(self):
    return __self.rightChild


  # Setting a new node
  def setElement(self, newElement):
    __self.element = newElement

  # Setting a new leftChild of the node
  def setLeftChild(self, newLeft):
    __self.leftChild = newLeft

  # Setting a new rightChild of the node
  def setRightChild(self, newRight):
    __self.rightChild = newRight

  # This function checks if the node has no children
  def isLeaf(self):
    return __self.leftChild == None and __self.rightChild == None

  # This function checks if the tree is empty (iff the tree contains no elements)
  def isEmpty(self):
    return root == None

  # This function inserts a new node (either left or right child)
  def insertNode(self, newNode):
    node = self.getElement()
    if node is not None:
      if newNode < node:
          if __self.leftChild is None:
              self.setLeftChild(BTNode(newNode))
          else:
              __self.leftChild.insertNode(newNode)
      elif newNode >= node:
          if self.rightChild is None:
              self.setRightChild(BTNode(newNode))
          else:
              __self.rightChild.insertNode(BTNode(newNode))
      else:
          self.setElement(BTNode(newNode))


  def getAllNodes(self, element):
    element = self.getElement()
    leftChildren = None
    rightChildren = None
    if not element.isLeaf():
      leftC = element.getLeft()
      if not leftC.isLeaf():
        leftChildren = leftC.getAllNodes()
        rightC = self.getRight()
        if rightC is not None:
          if not rightC.isLeaf():
            rightChildren = rightC.getAllNodes()        
            return [element, leftChildren, rightChildren]  
            return [element, leftChildren, rightC]
          return [element, leftChildren]
        return[element, leftC]
      return [element]



# This function calls the another to insert all the nodes in the tree
def insertNodes(node, list):
  for element in list:
    node.insertNode(element)

# This function calls another to get all the nodes of the tree
def getNodes(node):
  return node.getAllNodes()


# The main function. It creates a binary tree from a given list.
# Then returns the result of that binary tree (a new list in Binary Tree order).
def makeBinaryTree(list):
  root = BTNode(list[Math.round(len(list)/2)])
  list.remove(root)
  insertNodes(root, list)
  finalRes = getNodes(root)
  return finalRes

# Class Binary Tree (extends BTNode)

# class BinaryTree(BTNode):
  
#   # The constructor of the tree
#   def __ini__(self, element):
#     #  The root of the tree
#     self.root = BTNode(element)


print(makeBinaryTree([1, 2, 2, 6, 7, 5]))





