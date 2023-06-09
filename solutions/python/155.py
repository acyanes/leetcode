class Node:
    def __init__(self, val=None, _next=None):
        self.val = val
        self._min = math.inf
        self._next = _next

class LL:
    def __init__(self):
        self.node = Node(0)
        

    def push(self, val):
        if self.node._next:
            curr = self.node._next
            newVal = Node(val, curr)
            newVal._min = min(val, curr._min)
            self.node._next = newVal
        else:
            self.node._next = Node(val)
            self.node._next._min = val

    def pop(self):
        self.node._next = self.node._next._next

    def top(self):
        return self.node._next.val

    def getMin(self):
        return self.node._next._min
        

class MinStack:
    def __init__(self):
        self.stack = LL()
        

    def push(self, val: int) -> None:
        self.stack.push(val)

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack.top()
        

    def getMin(self) -> int:
        return self.stack.getMin()
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()