# Depth First Search 

## Core Concept
- Go deep
- Explore as far as possible down one path before backtracking

## Think of It Like This
- Navigating through a maze, you come to an intersection
- Take one path
- Once you hit a dead end, retrace steps to last intersection
- Take the next available path
- Repeat

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
- Stack
#### Algorithm
- Given a grid m and a starting row and column r and c:
    - Create a stack and push r and c on to it
    - Until the stack is empty:
        - Pop a row, col pair
        - Check if this position has been visited
        - If not, mark it as visited 
        - For the 4 adjacent positions of m\[r\]\[c\]:
            - If the position is valid (within the bounds of the grid), push it to the stack to search next

### Recursive + Adjacency Matrix
#### Main Data Structured Used
- Call stack
#### Algorithm
- Given a grid m, a starting row and column r and c:
    - If r, c are invalid or r,c have been visited, return
    - Else:
        - Mark position r,c as visited
        - Recursively explore the 4 neighbors

