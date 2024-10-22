from collections import deque

def breadth_first_search(graph, source, target):
    explored = set()
    queue = deque([(source, [source])])

    while queue:
        node, path_so_far = queue.popleft()
        print(f"Exploring: {node}")

        if node == target:
            print(f"Success! Reached {target}.")
            print("Found Path:", " -> ".join(path_so_far))
            return True

        if node not in explored:
            explored.add(node)

            for neighbor in graph.get(node, []):
                if neighbor not in explored:
                    queue.append((neighbor, path_so_far + [neighbor]))

    print(f"{target} could not be reached.")
    return False

graph = {
    'S': ['A', 'B'],
    'A': ['D', 'B'],
    'B': ['A', 'C'],
    'C': ['E'],
    'D': ['G'],
    'E': [],
    'G': []
}

breadth_first_search(graph, 'S', 'G')