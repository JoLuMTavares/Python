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
  # def __init__(__self, node):
  #   __self.leftChild = node.getLeft()
  #   __self.rightChild = node.getRight()
  #   __self.element = node.getValue()
    

  # Constructor of the binary tree  
  def __init__(__self, theElementValue, leftNode=None, rightNode=None, parentNode=None):
    __self.leftChild = leftNode
    __self.rightChild = rightNode
    __self.elementValue = theValueValue
    __self.parent = parentNode


  # Getting the current node
  def getValue(__self):
    return __self.elementValue

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
  def setValue(__self, newElementValue):
    __self.elementValue = newElementValue

  # Setting a new leftChild of the node
  def setLeftChild(__self, newLeft):
    __self.leftChild = newLeft

  # Setting the leftChild by the given value 
  def setLeftChildByValue(__self, newLeft):
    __self.leftChild = BTNode(newLeft)

  # Setting a new rightChild of the node
  def setRightChild(__self, newRight):
    __self.rightChild = newRight

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
  def delRightChild(__self):
    __self.rightChild = None


  # This function checks if the node has no children
  def isLeaf(self):
    return self.getLeft() == None

 
  

# Class Binary Tree (extends class BTNode)
def class BinaryTree(BTNode):

  # The root of the tree
  root = None

  # Array that keeps the values of all the nodes of the tree
  BTArray = []

  # Constructor
  def __init__(self, rootValue):
    root = BTNode(rootValue)
    BTArray.append(rootValue)

  # This function checks if the tree is empty (iff the tree contains no elements)
  def isEmpty(self):
    return root == None

  # This function makes the insertion of a left child of the root. For each
  # given value, the operation is made depending if the node is a leaf or has
  # no right child of have both left and right children. 
  def insertLeftNode(self, node, newNodeValue, currHeight , totalHeight):
    # When the node is a leaf, a new child is created with the value of
    # the current node and the node stores then the new given value
    if node.isLeaf():
      node.setLeftChildByValue(node.getValue())
      BTArray.append(node.getValue()) # New value at the end of the array
      node.setValue(newNodeValue) # New value for the current node
      BTArray[BTArray.index(node.getValue())] = newNodeValue # The first value stored is changed to the new given one
      currHeight += 1
      return 1
    # For the right child, is the same procedure as the left child  
    elif node.getRight() is None:
      # Very important is the total height of the three is more than 3, we
      # store the new given value as the right child and there's no switch
      if totalHeight == 3:
        node.setRightChildByValue(node.getValue())
        BTArray.append(node.getValue()) # New value at the end of the array
        node.setValue(newNodeValue) # New value for the current node
        BTArray[1] = newNodeValue # The current value of the node is also updated in the array
        return 0
      else:
        node.setRightChildByValue(newNodeValue)
        currHeight += 1
        BTArray.insert((2**(currHeight-1))-1, newNodeValue) # Inserting at the correct position according go the current (not total) height of the tree
        return 0
    elif (currHeight + 1) == totalHeight:
      # If the total height is now three, the tree grows and the left child of
      # the current node is the node it self. The node sets the new given value
      # as its element now.
      if totalHeight == 3:
        newLeftC = BTNode(node.getValue())
        newLeftC.setLeftChild(node.getLeft())
        newLeftC.setRightChild(node.getRight())
        node.setLeftChild(newLeftC)
        node.setValue(newNodeValue)
        node.delRightChild()
        currHeight += 1
        BTArray.insert(1, newNodeValue) # Insertion on position one
        return 1  
      # If the height of the tree is greater than 3, then no insertion can be 
      # can be made, since we reach the bottom of the tree.  
      return 2
    else:
      rightC = node.getRight()
      currHeight += 1
      # Here we use the recursivity
      insertRes = rightC.insertLeftNode(rightC, newNodeValue, currHeight, totalHeight)
      # If it wasn't possible any insertion, we go up
      if insertRes == 2 and currHeight > 2:
        currHeight -= 1
        return insertRes
      elif insertRes == 2 and currHeight == 2:
        # If no insertion was made and we came back to the position where
        # current height is two (left child of the root), the tree grows then.
        newLeftC = BTNode(node)
        node.setLeftChild(newLeftC)
        node.setValue(newNodeValue)
        node.delRightChild()
        currHeight += 1
        BTArray.insert(1, newNodeValue) # Insertion on position one
        return 1
      # If everything fails, we return 0
      return 0

  # This function inserts the node on the right children side of the root
  def insertRightNode(self, node, newNodeValue, currHeight, totalRightHeight):
    if node.isLeaf():
      node.setLeftChildByValue(node.getValue())
      node.setValue(newNodeValue)
      currHeight += 1
      return 1
    elif node.getRight() is None:
      node.setRightChildByValue(newNodeValue)      
      currHeight += 1
      return 0
    elif node.getLeft().isLeaf():
      if currHeight == 2:
        newLeftC = BTNode(node.getValue())
        newLeftC.setLeftChild(node.getLeft())
        newLeftC.setRightChild(node.getRight())
        node.setLeftChild(newLeftC)
        node.setValue(newNodeValue)
        node.delRightChild()
        currHeight += 1
        return 1
      return 2
    else:
      rightC = node.getRight()
      currHeight += 1
      insertRes = rightC.insertRightNode(rightC, newNodeValue, currHeight, totalRightHeight)
      if insertRes == 2 and currHeight > 2:
        currHeight -= 1
        return insertRes
      elif insertRes == 2 and currHeight == 2:
        newLeftC = BTNode(node)
        node.setLeftChild(newLeftC)
        node.setValue(newNodeValue)
        node.delRightChild()
        currHeight += 1
        return 1
      return 0

        


  # This function inserts elements as left children of the root
  def insertLeftChildren(self, node, newNodeValue, totalHeight):
    leftC = node.getLeft()
    if leftC is None:
      node.setLeftChildByValue(newNodeValue)
      BTArray.append(leftC.getValue())
      return True
    else:
      insertionRes = node.insertLeftNode(leftC, newNodeValue, 2, totalHeight)
      if insertionRes == 1:
        return True
      else:
        return False

  # This function inserts elements as right children of the root
  def insertRightChildren(self, node, newNodeValue, totalRightHeight):
    rightC = node.getRight()
    if rightC is None:
      node.setRightChildByValue(newNodeValue)
      BTArray.append(rightC.getValue())
      return True
    else:
      rightInsertion = node.insertRightNode(rightC, newNodeValue, 2, totalRightHeight)
      if rightInsertion == 1:
        return True
      return False

  # This function returns all the nodes from the Complete Binary Tree
  def getNodes(self, node):
    BTArray = []
    if not node.isLeaf():
      leftC = node.getLeft()
      BTArray.append(leftC.getValue())
      rightC = node.getRight()
      if not rightC == None:
        BTArray.append(rightC.getValue())
      BTArray.extend(leftC.getNodes(leftC))
      if not rightC == None and not rightC.isLeaf():
        BTArray.extend(rightC.getNodes(rightC))
    return BTArray

# This function calls the another to insert all the nodes in the tree
def insertNodes(correctPos, list):
  totalHeight = 1
  totalRightHeight = 1
  for i in range(0, correctPos):
    insRes = root.insertLeftChildren(root, list[i], totalHeight)
    if insRes == True:
      totalHeight += 1
  for j in range(correctPos, len(list)):
    rightIns = root.insertRightChildren(root, list[j], totalRightHeight)
    if rightIns == True:
      totalRightHeight += 1

# This function returns the array with the values of all the inserted nodes
def getNodeValuesArray(self):
  return BTArray


# The main function. It creates a binary tree from a given list.
# Then returns the result of that binary tree (a new list in Breath-first order).
def complete_binary_tree(list):
  rootPos = round(2*len(list)/3) - 1
  rootValue = list[rootPos]
  list.remove(rootValue)
  # insertNodes(rootPos, root, list)
  BTArray = [rootValue]
  BTree = BinaryTree(rootValue)
  BTree.insertNodes(rootPos, list)
  # BTArray.extend(root.getNodes(root))
  # finalRes = root.getNodes(root)
  return BTArray 

# print(complete_binary_tree([1, 2, 2, 6, 7, 5]))
print(complete_binary_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))





