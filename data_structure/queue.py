
class Queue :
    def __init__(self):
        self.list = list()

    def enqueue(self, data):
        self.list.append(data)


    def dequeue(self):
        first = self.list[0]
        del self.list[0]
        return first

## main

queue = Queue()

[queue.enqueue(i) for i in range(1,11)]

print(queue.list)
for i in range(len(queue.list)):
    print(queue.dequeue())

print(queue.list)

