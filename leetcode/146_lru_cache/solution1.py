class LinkedNode:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node: LinkedNode):
        node.next = None
        node.prev = None
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def delete(self, node: LinkedNode):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.next = None
        node.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.list_ = LinkedList()
        self.keys = {}
        self.cap = capacity

    def _insert(self, key: int, val: int):
        node = LinkedNode(key, val)
        self.list_.insert(node)
        self.keys[key] = node

    def get(self, key: int):
        if key in self.keys:
            val = self.keys[key].val
            self.list_.delete(self.keys[key])
            self._insert(key, val)
            return val

        return -1

    def put(self, key: int, value: int):
        if key in self.keys:
            self.list_.delete(self.keys[key])
        elif len(self.keys) == self.cap:
            del self.keys[self.list_.head.key]
            self.list_.delete(self.list_.head)
        self._insert(key, value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
