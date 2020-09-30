class Node :
    def __init__( self, data, prev=None, next=None ):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = None

    # tail 로 삽입
    def insert(self,data):
        # 헤드가 없을때
        if not self.head :
            self.head = Node(data)
            self.tail = self.head
            return True 
        # 헤드랑 테일이 같을 때 
        elif self.head == self.tail : 
            self.tail = Node(data) 
            self.tail.prev = self.head
            self.head.next = self.tail
            return True
        else :
            tail_temp = self.tail
            new_node = Node(data)
            tail_temp.next = new_node
            new_node.prev = tail_temp 
            self.tail = new_node
            return True

    # 특정 데이터 앞에 삽입
    def insert_before(self, data, insert_data):
        if not self.head :
            print("해당 데이터가 존재하지 않습니다. ", data)
            return False
        # head 앞에 삽입
        elif self.head.data == data :
            temp_head = self.head
            new_node = Node(insert_data)
            temp_head.prev = new_node
            new_node.next = temp_head
            self.head = new_node
            return True
        else :
            current_node = self.head
            while current_node:
                if current_node.data == data:
                    new_node = Node(insert_data)
                    new_node_before = current_node.prev
                    new_node_before.next = new_node
                    new_node.prev = new_node_before
                    new_node.next = current_node
                    current_node.prev = new_node
                    return True
                else :
                    current_node = current_node.next
            return False
        
    def search_from_tail(self,data):
        if not self.head :
            print("데이터가 존재하지 않습니다")
            return False
        current_node = self.tail
        while current_node : 
            if current_node.data == data:
                return True
            else :
                current_node = current_node.prev


    def desc(self):
        if not self.head :
            print("데이터가 존재하지 않습니다")
            return False
        current_node = self.head
        while current_node : 
            print(current_node.data)
            current_node = current_node.next

    def desc_from_tail(self):
        if not self.head :
            print("데이터가 존재하지 않습니다")
            return False
        current_node = self.tail
        while current_node :
            print(current_node.data)
            current_node = current_node.prev
        
### main ###
dbl = DoublyLinkedList() 
dbl.desc_from_tail()
for i in range(1,11):
    print(dbl.insert(i))

print(dbl.insert_before(5,4.5))
print(dbl.insert_before(4.5,100))
print(dbl.insert_before(1,0))
print(dbl.insert_before(10,11))

print("###### desc from head ######")
dbl.desc()
print("###### desc from tail ######")
dbl.desc_from_tail()
print("###### search from tail ######")
print(dbl.search_from_tail(10))



        


        

        
        
