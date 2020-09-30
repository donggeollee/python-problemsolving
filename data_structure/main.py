import sys
import os
sys.path.append("C:\\DEV\\PYTHON\\sources\\data_structure")
import binarySearchTree

print("#######################")
node = binarySearchTree.Node(21)
binary_search_tree = binarySearchTree.BinarySearchTree(node)

binary_search_tree.insert(14)
binary_search_tree.insert(11)
binary_search_tree.insert(18)
binary_search_tree.insert(28)
binary_search_tree.insert(25)
binary_search_tree.insert(32)
binary_search_tree.insert(5)
binary_search_tree.insert(12)
binary_search_tree.insert(15)
binary_search_tree.insert(19)
binary_search_tree.insert(23)
binary_search_tree.insert(27)
binary_search_tree.insert(30)
binary_search_tree.insert(37)
binary_search_tree.insert(7)

print(binary_search_tree.search(14))
print(binary_search_tree.search(11))
print(binary_search_tree.search(18))
print(binary_search_tree.search(1))
print(binary_search_tree.search(2))
print(binary_search_tree.search(3))
print(binary_search_tree.search(4))
print(binary_search_tree.search(23))
print(binary_search_tree.search(27))
print(binary_search_tree.search(30))
print(binary_search_tree.search(37))
print(binary_search_tree.search(7)) 

# 터미널 노드 삭제
print(" ####### delete(19) ####### ", binary_search_tree.delete(19) )

# 자식 노드 1개인 노드 삭제
print(" ####### delete(5) ####### ", binary_search_tree.delete(5) )

# 자식 노드 2개인 노드 삭제
print(" ####### delete(23) ####### ", binary_search_tree.delete(23) )
print(" ####### delete(27) ####### ", binary_search_tree.delete(27) )

print(binary_search_tree.search(5))
print(binary_search_tree.search(7))
print(binary_search_tree.search(23))
print(binary_search_tree.search(25))
print(binary_search_tree.search(19))








