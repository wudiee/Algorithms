class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
    
class BinaryTree():
  def __init__(self): #make tree
    self.root = None
  #preorder
  def preorder(self,n,cnt):
    if n=='A':
      cnt= 0
    
    if n !=None:
      print('-'*cnt,end = "")
      print(n.data)
      if n.left:
        cnt += 1
        self.preorder(n.left,cnt)
      if n.left != None:
        if n.right:
          cnt += 1
          self.preorder(n.right,cnt-1)
      if n.left == None:
        if n.right:
          cnt+=1
          self.preorder(n.right,cnt)
tree = BinaryTree()
n1 = Node('A')
n2 = Node('B')
n3 = Node('C')
n4 = Node('D')
n5 = Node('E')
n6 = Node('F')
n7 = Node('G')
n8 = Node('H')
n9 = Node('I')

tree.root = n1
n1.left = n2
n1.right = n7
n2.left = n3
n2.right = n4
n4.left = n5
n4.right = n6
n7.right = n8
n8.right = n9

print("preorder : ")
tree.preorder(tree.root,0)          
