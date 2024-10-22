from typing import List, Tuple, Dict

def depth_first_search(graph: Dict[str, List[str]], start: str, goal: str) -> List[str]:
    
    stack = [[start]]
    
    while stack:
        current_path = stack.pop()
        current_node = current_path[-1]
        
        if current_node == goal:
            return current_path
        
        for neighbor in graph.get(current_node, []):
            if neighbor not in current_path:
                new_path = current_path + [neighbor]
                stack.append(new_path)
                
    return None

example_graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}
start_node = 'A'
goal_node = 'G'
result = depth_first_search(example_graph, start_node, goal_node)
print(result)

