import collections

class StackMachine:
    
    def __init__(self):
        self.stack = collections.deque()
        
    def push(self, element):
        self.stack.append(element)
        
    def pop(self):
        self.stack.pop()
        
    def pop_and_print(self):
        print(self.stack.pop())
        
    def add(self):
        if len(self.stack) < 2:
            return
        x1, x2 = self.stack.pop(), self.stack.pop()
        if type(x1) == int and type(x2) == int:
            self.stack.appendleft(x1 + x2)
        else:
            self.stack.appendleft(str(x1) + str(x2))
            
# Test cases

sm = StackMachine()

sm.push(1)
sm.push(2)
sm.push("3")
sm.push(4)
sm.push(5)

sm.add()
print(sm.stack)
sm.add()
print(sm.stack)
sm.add()
print(sm.stack)
sm.add()
print(sm.stack)
