
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        # Head 노드가 없다면 초기화
        if not self.head: 
            self.head = Node(data)
            return True
        current_node = self.head
        # 마지막 노드 탐색 -> 다음 노드가 없을 때까지 순회
        while current_node.next :
            current_node = current_node.next
        current_node.next = Node(data)

    def search(self, data):
        current_node = self.head
        while current_node :
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False

    def delete(self, data):
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
            return True
        
        current_node = self.head

        if current_node.next :
            while current_node.next :
                if current_node.next.data == data:
                    temp = current_node.next
                    current_node.next = current_node.next.next
                    del temp
                    return True
                else :
                    current_node = current_node.next
        else :
            if current_node.data == data:
                del current_node

    def desc(self):
        current_node = self.head
        while current_node :
            print(current_node.data)
            current_node = current_node.next


# main 
linkedlist = LinkedList()

## 데이터 삽입 -> 맨 뒤 노드로 삽입
for i in range(1,11):
    linkedlist.insert(i)
    
## 링크드 리스트 전체 조회
linkedlist.desc()

## 데이터 5 조회
print("##########")
print(linkedlist.search(5)) # True
print("##########")

# 데이터 삭제 
linkedlist.delete(1) # Head
linkedlist.delete(5)
linkedlist.delete(7)
linkedlist.delete(10) # Tail

linkedlist.desc()





        