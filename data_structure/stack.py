
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        last_in = self.stack[-1]
        del self.stack[-1]
        return last_in

## main 
stack = Stack()
for i in range(1, 11):
    stack.push(i)

print(stack.stack)

for i in range(len(stack.stack)):
    print(stack.pop())

print(stack.stack)
