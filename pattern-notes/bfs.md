# Breadth First Search 

## Core Concept
- Go wide
- Explore all neighbors at the current depth before moving deeper

## Think of It Like This
- Navigating through a maze, you come to an intersection
- Look at **all** immediate paths available from that intersection
- Explore each one step forward
- Only after all paths at that distance are explored, move further out
- Repeat level by level

## Graph Implementation(s)

### Adjacency Matrix
#### How is the graph represented?
- 2D array
- The value in each cell represents a possible edge from Node i to Node j (1 or 0)
#### How is the algorithm implemented?
- Given a node *U*
    - To find neighbors of *U*, iterate through m\[*u*\]
    - If column *j* of m\[*u*\] has a 1, then an edge exists from *U* to *J*, and vice versa

### Adjacency List
#### How is the graph represented?
- Hash map
- Keys are nodes, values are lists of neighbors or an array of linked lists
#### How is the algorithm implemented?


## Solution Implementation(s)
>==**IMPORTANT NOTE**: For ALL methods, you need to keep track of visited nodes==

### Iterative + Adjacency Matrix
#### Main Data Structure Used
- Queue
#### Algorithm
- Given a grid m and a starting row and column r and c:
    - Create a queue and enqueue r and c
    - Until the queue is empty:
        - Dequeue a row, col pair
        - Check if this position has been visited
        - If not, mark it as visited
        - For the 4 adjacent positions of m\[r\]\[c\]:
            - If the position is valid (within the bounds of the grid), enqueue it to be explored later
