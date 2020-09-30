
# Binary Search Tree :: 이분탐색트리 노드 구현
class Node :
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head 
        while True : 
            if self.current_node.data == None : 
                self.head = Node(value)
                return True
            elif value < self.current_node.data : 
                if self.current_node.left != None :
                    self.current_node = self.current_node.left
                else : 
                    self.current_node.left = Node(value)
                    break
            else : 
                if self.current_node.right != None :
                    self.current_node = self.current_node.right
                else : 
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node : 
            if self.current_node.data == value :
                print(self.current_node.data)
                return True
            elif self.current_node.data < value :
                print(self.current_node.data)
                self.current_node = self.current_node.right
            else : 
                print(self.current_node.data)
                self.current_node = self.current_node.left
        return False

    def delete(self, value):
        searched = False
        self.current_node = self.head
        self.parent_node = self.head
        
        # 삭제할 데이터 찾기
        while self.current_node :
            if self.current_node.data == value: 
                searched = True
                break
            elif self.current_node.data < value: 
                self.parent_node = self.current_node
                self.current_node = self.current_node.right
            else :  
                self.parent_node = self.current_node
                self.current_node = self.current_node.left
        
        if searched == False : 
            print("해당 데이터가 없습니다.")
            return False

        # child node 가 0개인 node 삭제
        if not self.current_node.left and not self.current_node.right :
            if self.parent_node.data < self.current_node.data :
                self.parent_node.right = None
            else :
                self.parent_node.left = None
            del self.current_node 
            return True

        # child node 가 1개인 node 삭제
        if not self.current_node.left and self.current_node.right :
            if self.parent_node.data < self.current_node.data :
                self.parent_node.right = self.current_node.right
            else :
                self.parent_node.left = self.current_node.right
            del self.current_node 
            return True
        elif self.current_node.left and not self.current_node.right :
            if self.parent_node.data < self.current_node :
                self.parent_node.right = self.current_node.left
            else :
                self.parent_node.left = self.current_node.left
            del self.current_node 
            return True

        # child node 가 2개인 node 삭제
        ## 경우의 수 
            # 삭제할 노드가 부모노드의 오른쪽에 있을 때     
            # 삭제할 노드가 부모노드의 왼쪽에 있을 때
        ## 구현 전략 2가지
            # 1. 삭제할 노드를 삭제할 노드의 왼쪽 자식 중 가장 큰 값으로 대체
            # 2. 삭제할 노드를 삭제할 노드의 오른쪽 자식 중 가장 작은 값으로 대체
        ## 2번 번략을 사용한다고 했을 때 경우의 수 
            # 가장 작은 노드가 자식 노드를 가지고 있지 않을 때 
            # 가장 작은 노드가 오른쪽 자식노드를 가지고 있을 때.(왼쪽 자식은 있을 수 없음)
        
        if self.current_node.left and self.current_node.right :
            # 삭제할 노드가 부모노드의 '오른쪽'에 있을 때 
            if  self.parent_node.data < self.current_node.data : 
                # 오른쪽 노드중 가장 작은 값을 탐색
                change_node = self.current_node.right
                change_parent_node = self.current_node.right
                while change_node.left :
                    change_parent_node = change_node 
                    change_node = change_node.left
                # 가장 작은 노드가 오른쪽 자식 노드가 있을 경우
                if change_node.right :
                    change_parent_node.left = change_node.right
                else :
                    change_parent_node.left = None
                self.parent_node.right = change_node
                change_node.right = self.current_node.right
                change_node.left = self.current_node.left      

            # 삭제할 노드가 부모노드의 '왼쪽'에 있을 때 
            else :
                # 오른쪽 노드중 가장 작은 값을 탐색
                change_node = self.current_node.right
                change_parent_node = self.current_node.right
                while change_node.left :
                    change_parent_node = change_node
                    change_node = change_node.left
                # 가장 작은 값이 오른쪽 자식 노드가 있을 경우
                if change_node.right :
                    change_parent_node.left = change_node.right
                else :
                    change_parent_node.left = None
                self.parent_node.left = change_node
                change_node.right = self.current_node.right
                change_node.left = self.current_node.left  
            
            del self.current_node
            return True
                




                

                






