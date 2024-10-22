import preq
from typing import List, Tuple, Dict

def british_museum_search(graph: Dict[str, List[str]], start: str, goal: str) -> List[str]:
    
    all_paths = []
    
    def find_all_paths(current_path: List[str]) -> None:
        current_node = current_path[-1]
        if current_node == goal:
            all_paths.append(current_path.copy())
            return
        for neighbor in graph.get(current_node, []):
            if neighbor not in current_path:
                current_path.append(neighbor)
                find_all_paths(current_path)
                current_path.pop()
                
    find_all_paths([start])
    
    if all_paths:
        shortest_path = min(all_paths, key=len)
        return shortest_path
    else:
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
result = british_museum_search(example_graph, start_node, goal_node)
print(f"The shortest path from {start_node} to {goal_node} is: {result}")