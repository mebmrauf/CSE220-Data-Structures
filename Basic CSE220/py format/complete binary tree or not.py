class BTNode:
  def __init__(self, elem):
    self.elem = elem
    self.right = None
    self.left = None

#Array to Binary Tree
def tree_construction(arr, i = 1):
  if i>=len(arr) or arr[i] == None:
    return None
  p = BTNode(arr[i])
  p.left = tree_construction(arr, 2*i)
  p.right = tree_construction(arr, 2*i+1)
  return p

#No of nodes
def noOfNodes(root):
    if root == None:
        return 0
    return 1+noOfNodes(root.left)+noOfNodes(root.right)

#Complete binary tree or not
def completeTree(root,i=0):
    totalNodes = noOfNodes(root)
    if root == None:
        return True
    if i >= totalNodes:
        return False
    return (completeTree(root.left,2*i+1) and completeTree(root.right,2*i+2))

root = tree_construction([None, 71, 50, 90, 20, None, None, 98, None, 40, None, None, None, None, 94, None])
result = completeTree(root)
if result == True:
    print("Complete binary tree.")
else:
    print("Not a complete binary tree.") 