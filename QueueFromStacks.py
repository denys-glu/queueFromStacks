class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    # challenge for you guys
    def Push(self, val):
        newnode = Node(val)
        newnode.next = self.head
        self.head = newnode
        return self

    def Pop(self):
        if self.head == None:
            print("Stack is empty")
        
        toReturn = self.head
        self.head = toReturn.next
        return toReturn

    def Peek(self):
        if self.head == None:
            print("Stack is empty")
            return self.head
        else:
            # print(self.head.value)
            return self.head.value

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def size(self):
        walker = self.head
        size = 0

        while walker != None:
            size += 1
            walker = walker.next

        return size


# Create a Queue using 2 stacks. A hint: stack1 will hold the contents of the actual queue, stack2 will be used in the enQueueing
# Efficiency is not the goal!
# Efficiency is not the goal!
# Efficiency is not the goal!
# The goal is to practice using one data structure to implement another one, in our case Queue from 2 Stacks
# Queue is FIFO --> First In First out
# Stack is LIFO --> Last  In First Out
class QueueOfStacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def front(self):
        print("front is: ", self.stack1.Peek())
        return self.stack1.Peek()
    
    def isEmpty(self):
        if self.stack1.isEmpty():
            print("qs is empty")
            return True
        print("qs is NOT empty")
        return False

    def size(self):
        print(self.stack1.size())
        return self.stack1.size()

    def deQueue(self):
        if self.stack1.isEmpty():
            return "Queue is empty."
        
        return self.stack1.Pop()

    def enQueue(self, value): 

        while self.stack1.isEmpty() == False:
            self.stack2.Push(self.stack1.Pop().value)
        

        self.stack1.Push(value)

        while self.stack2.isEmpty() == False:
            self.stack1.Push(self.stack2.Pop().value)
        
        
        return self
    # Optional
    def showQS(self):
        if self.stack1.head == None:
            print("QS is empty from showQS")
            return self

        walker = self.stack1.head

        while walker != None:
            print(walker.value)
            walker = walker.next
        
        return self



qs = QueueOfStacks()

qs.enQueue("first")
qs.enQueue("second")
qs.enQueue("third")
qs.front()
qs.showQS()
print("="*40)
qs.deQueue()
qs.front()
qs.showQS()
# qs.deQueue()
# qs.deQueue()
# qs.showQS()
# qs.isEmpty()
# print("="*40)
# qs.enQueue("new")
# qs.front()
# qs.showQS()
# print("="*40)
# qs.deQueue()
# qs.showQS()
# print("="*40)
# qs.enQueue("first")
# qs.enQueue("second")
# qs.enQueue("third")
# qs.front()
# qs.showQS()
