# Number of Islands

## OUTCOME
==***Failure***==

Iterative Approach
### Optimal Pattern (from solution)
> What pattern is used in the optimal solution?

- DFS or BFS

### Why My Attempt Failed
> What approach did I try?
> Where did it break down?
> What assumption was wrong?

- I really could not form an approach to begin with due to my lack of understanding of DFS/BFS. I tried using two nested loops to check for the existence of a 1. Thats about as far as I got.

### The Key Idea (one paragraph)
> What is the main trick that makes this work?
> Why does this avoid brute force?

-

### What Is Being Tracked?
> Variables, structs used for tracking state

==Answer Here==
- 

### When Do Things Change?
> What causes updates?
> What condition(s) forces adjustment?

==Answer Here==
- 


### One-Sentence Explanation
> If I had to explain this to somebody else

==Answer Here==
- 


## CODE

### DFS Iterative Solution
```Python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        For every cell that contains a 1 and hasnt been visited, 
        complete dfs on this cell using 1 indicating a valid path

        During dfs on a given cell, count the amount of newly visited nodes and return the final count 


        '''                    
        DIRS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        ROWS = len(grid)
        COLS = len(grid[0]) 
        visited = set()
        islands = {}
        def dfs(r, c): 
            island_size = 0
            stack = [(r, c)]

            while stack: 
                curr_row, curr_col = stack.pop()
                if (curr_row, curr_col) in visited: 
                    continue

                visited.add((curr_row, curr_col))
                island_size += 1
                for dr, dc in DIRS:
                    new_row, new_col = curr_row + dr, curr_col + dc
                    if 0 <= new_row < ROWS \
                    and 0 <= new_col < COLS \
                    and grid[new_row][new_col] == "1" \
                    and (new_row, new_col) not in visited: 
                       
                        stack.append((new_row, new_col))
            return island_size

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    # print("firing")
                    islands[(i, j)] = dfs(i, j)
        
        return len(islands)
```

### DFS Recursive solution
```Python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        For every cell that contains a 1 and hasnt been visited, 
        complete dfs on this cell using 1 indicating a valid path

        During dfs on a given cell, count the amount of newly visited nodes and return the final count 


        '''                    
        DIRS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        ROWS = len(grid)
        COLS = len(grid[0]) 
        
        visited = set()
        res = 0
        
        def dfs(r, c): 

            '''
            The logic of the recursive approach:
            - if this cell is out of bounds, has been seen, or is water:
                --> stop looking down this path
            - otherwise:
                --> mark the cell as seen
                --> try looking down all adjacent paths from this cell

            - once all function calls return from a root dfs call:
                --> we have reached the borders of an island, and can 
                    increment the number of islands
            '''
            if (r < 0 or c < 0 \
            or r >= ROWS or c >= COLS \
            or (r, c) in visited \
            or grid[r][c] == "0"):
                return

            
            visited.add((r, c))
            for dr, dc in DIRS: 
                dfs(r + dr, c + dc)
          
        
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    
                    dfs(i, j)
                    res += 1
        return res
```

### BFS Solution
```Python
```
