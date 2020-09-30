
# 힙 구현 by 배열
class Heap :
    def __init__(self):
        self.list = [0]

    def is_move_up(self, index):
        if index < 2 :
            return False

        parent_index = index//2
        if self.list[parent_index] < self.list[index]:
            return True
        else : 
            return False

    def is_move_down(self, index):
        left = index * 2
        right = index * 2 + 1
        # 자식 노드 둘 다 없을 때 
        if left >= len(self.list) :
            print("test1")
            return False
        # 왼쪽 노드만 있을 때 
        elif right >= len(self.list) : 
            print("test2")
            if self.list[left] > self.list[index]:
                return True
            else :
                return False
        # 자식노드 둘 다 있을 때 
        else : 
            print("test3")
            if self.list[left] > self.list[index] or self.list[right] > self.list[index]:
                return True
            else :
                return False
        print("test4")

    def push(self, data):
        self.list.append(data)

        inserted_index = len(self.list) - 1
        while self.is_move_up(inserted_index) :
            parent_index = inserted_index // 2
            self.list[inserted_index], self.list[parent_index] = self.list[parent_index], self.list[inserted_index]
            inserted_index = parent_index

    def pop(self):
        pop_data = self.list[1]

        last_index = len(self.list) - 1
        self.list[1] = self.list[last_index]
        del self.list[last_index]
        index = 1

        while self.is_move_down(index):
            left = index * 2
            right = index * 2 + 1
            # 왼쪽 자식노드만 있을 때 
            if self.list[left] and not self.list[right] :
                self.list[index], self.list[left] = self.list[left], self.list[index]
                index = left
            # 자식노드 둘다 있을 때 
            elif self.list[left] and  self.list[right] :
                if self.list[left] < self.list[right] :
                    self.list[index], self.list[right] = self.list[right] ,self.list[index]
                    index = right
                else :
                    self.list[index], self.list[left] = self.list[left] ,self.list[index]
                    index = left
        return pop_data

heap = Heap()
[heap.push(i) for i in range(1,11)]
heap.push(11)
print(heap.list)

print("##### pop test #####")
print(heap.pop())
print(heap.list)
print("##### pop test #####")
print(heap.pop())
print(heap.list)
print("##### pop test #####")
print(heap.pop())
print(heap.list)