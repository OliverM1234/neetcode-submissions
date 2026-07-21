class Node:
    def __init__(self,key = 0,val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0

        self.tail = Node()
        self.head = Node(0,0,self.tail)
        self.tail.prev = self.head

        self.node_dict = {}
        

    def get(self, key: int) -> int:

        if key in self.node_dict:
            node = self.node_dict[key]

            node.prev.next = node.next
            node.next.prev = node.prev

            oldHead = self.head.next

            self.head.next = node
            node.prev = self.head
            node.next = oldHead
            oldHead.prev = node

            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.node_dict:

            oldNode = self.node_dict[key]

            oldNode.prev.next = oldNode.next
            oldNode.next.prev = oldNode.prev

            newNode = Node(key,value)
            
            oldHead = self.head.next

            self.head.next = newNode
            newNode.prev = self.head
            newNode.next = oldHead
            oldHead.prev = newNode

            self.node_dict[key] = newNode

        else:

            newNode = Node(key,value)
            
            oldHead = self.head.next

            self.head.next = newNode
            newNode.prev = self.head
            newNode.next = oldHead
            oldHead.prev = newNode


            if self.size == self.cap:

                del self.node_dict[self.tail.prev.key]

                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev

            else:

                self.size += 1

            self.node_dict[key] = newNode

        return None



        
