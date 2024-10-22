import heapq

def branch_and_bound(start, neighbors, costs, goal):
    pq = [(0, start, [start])]
    best_cost = {start: 0}
    
    while pq:
        current_cost, current_node, path = heapq.heappop(pq)
        
        print(f"Exploring node: {current_node} with current cost: {current_cost}, path: {path}")
        
        if current_node == goal:
            print(f"Goal reached with path: {path} and cost: {current_cost}")
            return path, current_cost
        
        for neighbor in neighbors.get(current_node, []):
            cost = current_cost + costs.get((current_node, neighbor), float('inf'))
            
            if neighbor not in best_cost or cost < best_cost[neighbor]:
                best_cost[neighbor] = cost
                heapq.heappush(pq, (cost, neighbor, path + [neighbor]))
                print(f"Branching to {neighbor} with cost: {cost}, new path: {path + [neighbor]}")
    
    print("Goal not reachable.")
    return None, float('inf')

if __name__ == "__main__":
    neighbors = {
        1: [2, 3],
        2: [4, 5],
        3: [5],
        4: [6],
        5: [6],
        6: []
    }

    costs = {
        (1, 2): 1, (1, 3): 4,
        (2, 4): 2, (2, 5): 5,
        (3, 5): 1,
        (4, 6): 3,
        (5, 6): 2
    }

    path, total_cost = branch_and_bound(1, neighbors, costs, 6)
    print(f"Best path: {path} with total cost: {total_cost}")