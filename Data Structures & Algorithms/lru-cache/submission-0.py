class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:
    

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}

        self.left=Node(0,0)
        self.right=Node(0,0)

        self.left.next=self.right
        self.right.prev=self.left
        
    def remove(self,node):
        previous=node.prev
        following=node.next

        previous.next=following
        following.prev=previous
    
    def insert(self,node):
        previous=self.right.prev
        following=self.right

        previous.next=node
        following.prev=node

        node.prev=previous
        node.next=following

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node=self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.val=value
            self.remove(node)
            self.insert(node)
        
        else:
            node=Node(key,value)
            self.cache[key]=node
            self.insert(node)

            if len(self.cache)> self.capacity:
                lru=self.left.next
                self.remove(lru)
                del self.cache[lru.key]

    
        
