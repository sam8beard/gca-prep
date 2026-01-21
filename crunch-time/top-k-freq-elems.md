# Top K Frequent Elements

## OUTCOME
==***Unoptimized Success***==

### What Is The Time Complexity Of MY Solution? 

- O(nlog(n))

### What Is The Bottleneck Of MY Solution?
> Nested loops, repeated scans, recursion overlap, etc.

- Iterating through all elements in the input list

### What Pattern Removes The Bottleneck?
> Hash map -> remove repeated scans
> Sliding window -> removes nested loops
> DP memoization -> removes recomputation
> Sorting + two pointers -> replaces brute force pairs

- Using bucket sort to group elements and index by frequency 

### What Signal In The Problem Hinted At That Pattern?
> Contiguous subarray, frequency counting, choices at each index, etc.

- Frequency counting

### Time Complexity Of The Optimal Solution

- O(n)

### Summary (1-2 sentences describing analysis above)

- I achieved a solution in O(nlog(n)) time. I iterated through all elements in the input list, while I could've used bucket sort to group values by frequency and then returning the first k elements of the buckets to achieve O(n) time.

