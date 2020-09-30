graph = dict()
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

def breadth_first_search(graph, start_data, search_data):

    visited_queue = list() # 방문한 노드 큐
    need_to_visit_queue = list() # 방문할 노드 큐

    need_to_visit_queue.append(start_data)
    
    big_O_count = 0
    while need_to_visit_queue : 
        big_O_count += 1
        vertex = need_to_visit_queue.pop(0)
        if vertex not in visited_queue:
            visited_queue.append(vertex)
            need_to_visit_queue.extend(graph[vertex])
    
    print(big_O_count)
    return visited_queue

print(breadth_first_search(graph,'A','B'))
