# CIA1

### 1. British Museum Search
The British Museum search is a brute-force search algorithm, where every possible solution is considered, similar to searching a large museum blindly. It is often used metaphorically to refer to an exhaustive, inefficient search.

### 2. Depth First Search (DFS)
Depth First Search is an algorithm that explores a graph or tree by diving as deep as possible into each branch before backtracking. It is commonly used for traversing or searching tree and graph data structures.

### 3. Breadth First Search (BFS)
Breadth First Search is a graph traversal algorithm that explores the graph level by level, visiting all the neighbors of a node before moving on to their children. It finds the shortest path in an unweighted graph.

### 4. Hill Climbing
Hill climbing is a heuristic search algorithm that moves towards the steepest ascent (i.e., the most promising direction) to find the optimal solution. It can get stuck in local maxima, so variations like simulated annealing are used to improve its performance.

### 5. Beam Search
Beam Search is a heuristic search algorithm that explores a graph by expanding only the top "k" most promising nodes at each level. It balances breadth-first and depth-first searches to limit memory usage.

### 6. Oracle
In computational terms, an oracle is a theoretical entity that can provide answers to specific decision problems in constant time. It is often used in discussions of complexity theory and is integral to the study of NP-complete problems.

### 7. Branch and Bound
Branch and Bound is a search algorithm used for solving optimization problems by dividing the problem into subproblems (branching) and using bounds to prune paths that can't yield better solutions. 

### 8. Branch and Bound Greedy
In this variation, a greedy approach is used to choose the next branch to explore, typically by selecting the most promising node according to some heuristic, potentially speeding up the solution process but not guaranteeing the optimal solution.

### 9. Branch and Bound Dead Horse (Fathoming or Pruning)
This refers to eliminating or "pruning" branches of the search tree that cannot possibly lead to a better solution, thus optimizing the search process by avoiding unnecessary work.

### 10. Branch and Bound Exit Early
In this technique, the algorithm terminates early if it finds a solution that satisfies the desired criteria or if further exploration of the tree won't lead to a better solution.

### 11. A* (A-Star) Algorithm
A* is an informed search algorithm that finds the shortest path between two nodes in a graph. It uses a heuristic function to prioritize nodes that appear to be closer to the goal, balancing exploration and exploitation.

### 12. AO* (And-Or) Algorithm
AO* is a search algorithm used in problem-solving that involves AND and OR graphs. It deals with problems that can be broken down into subproblems, where some subproblems need to be solved simultaneously (AND) and some alternatively (OR).

---

# CIA2

### 1. Minimax Algorithm
The Minimax algorithm is a recursive decision-making algorithm used in two-player games. It aims to minimize the possible loss for the worst-case scenario, assuming that the opponent is also playing optimally. The player maximizes their minimum gain.

### 2. Alpha-Beta Pruning
Alpha-Beta pruning is an optimization technique for the Minimax algorithm. It eliminates branches of the game tree that do not affect the final decision, thus improving the efficiency by reducing the number of nodes evaluated.
