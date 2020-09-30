
graph = {}
graph['A'] = ['B','C']
graph['B'] = ['A','D']
graph['C'] = ['A','G','H','I']
graph['D'] = ['B','E','F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C','J']
graph['J'] = ['I']

def depth_first_search(graph, start_node):
    visited_queue = list() # 방문한 노드 큐
    need_to_visit_stack = list() # 방문할 노드 스택
    need_to_visit_stack.append(start_node)
    while need_to_visit_stack :
        vertex = need_to_visit_stack.pop()
        if vertex not in visited_queue :
            visited_queue.append(vertex)
            # 방문할 리스트 스택에 담는 데이터 순서에 따라 다르게 탐색 할 수 있음
            # 하지만 DFS 에서 순서가 그렇게 중요한 것은 아님. 
            ### A - C 순서로 깊이 탐색  
            need_to_visit_stack.append(graph[vertex])
            ### A - B 순서로 깊이 탐색 
            # for i in range(1, len(graph[vertex])+1):
            #     need_to_visit_stack.append(graph[vertex][-i])
        
    return visited_queue

print(depth_first_search(graph,'A'))