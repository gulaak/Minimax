# MiniMax Algorithm

How to use algorithm

1. Instantiate GameTree , tree = GameTree()

2. Construct the tree , tree.constructTree()  # creates game tree of specified depth with randomized utilities at each terminal state

3. run the algorithm on tree, tree.minimax() # computes the decision at the root node and all decisions at each level

4. print out utilities at each terminal state, tree.bfs() # performs a breadth first search and prints all utility values
