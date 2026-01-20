# 3sum 

## OUTCOME
==***Failure***==

### Optimal Pattern (from solution)
> What pattern is used in the optimal solution?

- Two pointers

### Why My Attempt Failed
> What approach did I try?
> Where did it break down?
> What assumption was wrong?

- Barely could come up with an approach. I tried to first sort the nums array, use a dictionary to track sums, use a left pointer to keep track of a static value in nums, then iterate through nums, compute the difference of the current value and the left pointer value, then check if the difference existed in the dictionary
- It broke down when I assumed I could use the same complement approach as 2sum. I should've attempted to brute force at first.
- I assumed I could get the solution without using a nested loop

### The Key Idea (one paragraph)
> What is the main trick that makes this work?
> Why does this avoid brute force?

- The main trick to use two pointers and a fixed value. The left pointer starts just after the fixed value, and the right pointer starts at the end of nums. You then loop until the left or right pointer are at the same position. On each iteration, you compute the sum using the fixed value, the value at the left pointer, and the value at the right pointer. If the sum is greater than 0, move the right pointer to the left. If the sum is less than 0, move the left pointer to the right. If the sum is equal to 0, add a triplet containing these three values to the result, move both pointers inward, and skip duplicates at the left pointer. In order to skip duplicates in this case, we check if the new left pointer value is the same as the previous left pointer value, and that the left and right pointers are not at the same position yet. We then move the left pointer to the right until we find a new value.
- This avoids brute force by avoiding duplicates before sum evaluation to reduce the amount of total passes, and using the two pointers + fixed value to avoid checking every item in the array. Using brute force involves using 3 loops to check every possible combination of values that adhere to the constraint.

### What Is Being Tracked?
> Variables, structs used for tracking state

- currValue - A fixed value in the array
- left - A left pointer that begins after the currValue and moves right
- right - A right pointer that begins at the end of the array and moves left
- result - A list of triplets

### When Do Things Change?
> What causes updates?
> What condition(s) forces adjustment?

- Updates are made to the state when the sum of the three points is evaluated, when the left and right pointers close in on the same position, and when duplicates are detected


### One-Sentence Explanation
> If I had to explain this to somebody else

- This solution is achieved by sorting the array, using a fixed value along with two pointers, and then moving the pointers based on the evaluation of the sum of all three pointers and duplicates.
