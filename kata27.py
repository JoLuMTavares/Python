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
  def __init__(__self, theElement, leftNode=None, rightNode=None, parentNode=None):
    __self.leftChild = leftNode
    __self.rightChild = rightNode
    __self.element = theElement
    __self.parent = parentNode


  # Getting the current node
  def getValue(__self):
    return __self.element

  # Getting the left child of the node
  def getLeft(__self):
    return __self.leftChild

  # Getting the right child of the node
  def getRight(__self):
    return __self.rightChild

  # Getting the parent node
  def getParent(__self):
    return __self.parent


  # Setting a new node
  def setValue(__self, newElement):
    __self.element = BTNode(newElement)

  # Setting a new leftChild of the node
  def setLeftChild(__self, newLeft):
    __self.leftChild = newLeft

  # Setting the leftChild by the given value 
  def setLeftChildByValue(__self, newLeft):
    __self.leftChild = BTNode(newLeft)

  # Setting a new rightChild of the node
  def setRightChild(__self, newRight):
    __self.leftChild = newRight

  # Setting the rightChild by the given value
  def setRightChildByValue(__self, newRight):
    __self.rightChild = BTNode(newRight)

  # Setting the parent node
  def setParent(__self, parentNode):
    __self.parent = parentNode


  # Deleting left Child
  def delLeftChild(__self):
    __self.leftChild = None


  # Deleting right Child
  def delRighttChild(__self):
    __self.rightChild = None


  # This function checks if the node has no children
  def isLeaf(self):
    return self.getLeft() == None and self.getRight() == None

  # This function checks if the tree is empty (iff the tree contains no elements)
  def isEmpty(self):
    return self.getValue() == None

  # This function inserts a new node (either left or right child)
  """def insertNode(self, node, newNodeValue):
    if newNodeValue < node.getValue():
      leftC = node.getLeft()
      if leftC is None:
          node.setLeftChild(newNodeValue)
      else:
          leftC.insertNode(leftC, newNodeValue)
    else:
      rightC = node.getRight()
      if rightC is None:
          node.setRightChild(newNodeValue)
      else:
          rightC.insertNode(rightC, newNodeValue)
"""
  # New version of the function
  def insertNode(self, node, newNodeValue, height=0):
    if node.isLeaf():
      node.setLeftChildByValue(newNodeValue)
    elif node.getRight() is None:
      node.setRightChildByValue(node.getValue())
      node.setValue(newNodeValue)
    else:
      node.setLeftChild(node)
      node.setValue(newNodeValue)
      node.delRighttChild()



  # This function inserts elements as left children of the root
  def insertLeftChildren(self, node, newNodeValue):
    leftC = node.getLeft()
    if leftC is None:
      node.setLeftChild(newNodeValue)
    else:
      node.insertNode(leftC, newNodeValue, 1)

  # This function inserts elements as right children of the root
  def insertRightChildren(self, node, newNodeValue):
    rightC = node.getLeft()
    if rightC is None:
      node.setRightChild(newNodeValue)
    else:
      node.insertNode(rightC, newNodeValue, 1)

  # This function returns all the nodes from the Complete Binary Tree
  def getNodes(self, node):
    BTree = [node.getValue()]
    if not node.isLeaf():
      leftC = node.getLeft()
      BTree.append(leftC.getValue())
      rightC = node.getRight()
      if not rightC == None:
        BTree.append(rightC.getValue())
      BTree.extend(leftC.getNodes(leftC))
      if not rightC == None and not rightC.isLeaf():
        BTree.extend(rightC.getNodes(rightC))
    return BTree

# This function calls the another to insert all the nodes in the tree
def insertNodes(node, list):
  for element in list:
    node.insertNode(node, element)



# The main function. It creates a binary tree from a given list.
# Then returns the result of that binary tree (a new list in Binary Tree order).
def complete_binary_tree(list):
  root = BTNode(list[round(len(list)/2)])
  list.remove(root.getValue())
  insertNodes(root, list)
  finalRes = root.getNodes(root)
  return finalRes 



# print(makeBinaryTree([1, 2, 2, 6, 7, 5]))

print(complete_binary_tree([1, 2, 2, 6, 7, 5]))





