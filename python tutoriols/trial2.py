class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class  doublelinkedlist:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = Node
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

