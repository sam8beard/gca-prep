# Number of Islands

## OUTCOME
==***Failure***==

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

```Python
grid_1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid_2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]
visited = set()

def dfs(grid, r, c, rows, cols):
            island_size = 0
            print(f'Starting search from position {r, c}\n\n')
            stack = [(r, c)]
            while stack:
                curr_row, curr_col = stack.pop()
                if (curr_row, curr_col) in visited:
                    continue
                
                island_size += 1
                print(f'new neighbor found for {r, c}')
                visited.add((curr_row, curr_col))
                
                for dr, dc in directions:
                    new_row = curr_row + dr
                    new_col = curr_col + dc 
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == "1" and (new_row, new_col) not in visited:
                        
                        stack.append((new_row, new_col))
                    
            # # total edges from r -> c
            # print(f'Total edges from {r} -> {c}: {total_edges}\n\n')
            return island_size

def get_rows_and_cols(grid):
    return len(grid), len(grid[0])
    
def num_islands(grid):
    
    rows, cols = get_rows_and_cols(grid)
    island_sizes = {}
    for i in range(rows):
        for j in range(cols): 
            if grid[i][j] == "1" and (i, j) not in visited:
                island_sizes[(i, j)] = dfs(grid, i, j, rows, cols)
                print(island_sizes)

num_islands(grid_1)
```

