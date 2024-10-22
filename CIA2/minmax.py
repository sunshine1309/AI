import math

MAX_PLAYER = 1
MIN_PLAYER = -1

def minimax(depth, node_index, maximizing_player, values):
    if depth == 3:
        return values[node_index]
    
    if maximizing_player:
        max_eval = -math.inf
        for i in range(2):
            eval = minimax(depth + 1, node_index * 2 + i, False, values)
            max_eval = max(max_eval, eval)
        return max_eval
    
    else:
        min_eval = math.inf
        for i in range(2):
            eval = minimax(depth + 1, node_index * 2 + i, True, values)
            min_eval = min(min_eval, eval)
        return min_eval

if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    
    optimal_value = minimax(0, 0, True, values)
    
    print("The optimal value is:", optimal_value)
