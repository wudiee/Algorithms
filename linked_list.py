class Node:
  def __init__(self,data,loc,next = None):
    self.data = data
    self.loc = loc
    self.next = next
def init_list():
  global node1
  node1 = Node(5,0)
  node2 = Node(10,1)
  node3 = Node(17,2)
  node4 = Node(9,3)
  node5 = Node(13,4)
  node6 = Node(7,5)
  node7 = Node(19,6)

  node1.next = node2
  node2.next = node3
  node3.next = node4
  node4.next = node5
  node5.next = node6
  node6.next = node7
  
def print_list():
  global node1
  node = node1
  while node:
    print(node.data,end=" ")
    node = node.next
  
  def insert_node(data,loc):
  global node1
  new_node = Node(data,loc)
  node_p = node1
  node_t = node1

  while node_t.loc != new_node.loc:
    node_p = node_t
    node_t = node_t.next

  new_node.next = node_t
  node_p.next = new_node

if __name__ == "__main__":
  init_list()
  insert_node(33,4)
  print_list()

  
  
