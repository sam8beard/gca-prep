# Longest Substring Without Repeating Characters

## OUTCOME
==***Failure***==

### Optimal Pattern (from solution)
> What pattern is used in the optimal solution?

- Sliding window

### Why My Attempt Failed
> What approach did I try?
> Where did it break down?
> What assumption was wrong?

- I tried implementing a sliding window approach with a substring variable that that was only updated on each iteration if the current right pointer did not exist in the current substring. If it did, I reset the substring var and increased the left pointer by 1. I then returned the length of the substring var at the end of the function.
- It broke down/failed because I was using a string var for the substring when I should've have been using a set. I also mistakenly would update the max length found at the beginning of each iteration. This essentially resulted in an off-by-one error.
- I incorrectly assumed that I needed to completely clear the current longest substring each time a duplicate character was found. 

### The Key Idea (one paragraph)
> What is the main trick that makes this work?
> Why does this avoid brute force?

- The main trick that makes this work is using a while loop to clear all characters that match the current one from the set at the start of each iteration, and then increment the left pointer by one. 
- This avoids bruteforce by using a global set variable that is only updated in the event a duplicate character is found. This allows you to only have to remove a constant amount of duplicates, keeping the time complexity at O(n). The brute force uses a local set variable for each iteration and then a nested loop to add all non-duplicate characters within the current window size.

### What Is Being Tracked?
> Variables, structs used for tracking state

- charSet - a set of all characters in the longest substring w/o repeating chars
- l - a left pointer used to shrink the window size
- max_len - the length of the longest substring w/o repeating chars

### When Do Things Change?
> What causes updates?
> What condition(s) forces adjustment?

- If the current character is found in our set, it is removed and the window shrinks by incrementing the left pointer
- Else, the character is added to our set and max_len is updated with the greater value between the last max_len (largest so far) and the current window size


### One-Sentence Explanation
> If I had to explain this to somebody else

- The solution is derived by iterating through the string, clearing the set and shrinking the window from the left if the current character is in the set, and then adding the current character to our set, updating the max_len (largest window so far), then returing the max_len.
