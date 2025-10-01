class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.items[-1] 

    def is_empty(self):
        return len(self.items) == 0 

    def size(self):
        return len(self.items)  


# -------- โปรแกรมสำหรับทดสอบ --------
s = Stack()
print("Is empty?", s.is_empty())

for i in range(1, 6):
    s.push(i)

print("Size after push:", s.size())
print("Top element:", s.peek())

print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())

print("Is empty?", s.is_empty())
print("Pop from empty:", s.pop())
