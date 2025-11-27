# Longest Common Subsequence (LCS) – P Class Problem

## Objective
Demonstrate understanding of computational complexity by solving a problem from class **P**, creating a real-world scenario, and analyzing the algorithm.

---

## Problem Description
The **Longest Common Subsequence (LCS)** problem finds the longest sequence of elements that appear in two sequences in the same relative order (not necessarily contiguous).  

- **Class:** P (polynomial-time solvable)  
- **Algorithm:** Dynamic Programming  

---

## Real-World Scenario
A supermarket wants to analyze customer shopping behavior. By comparing two customers’ shopping lists, the store can find a common ordered pattern of items both purchased. This helps in designing **bundled offers**, optimizing product placement, and predicting customer behavior.

---

## Problem Instance

**Sequence A (Customer A):**  
Milk, Bread, Eggs, Butter, Cheese, Apples, Bananas, Yogurt, Coffee, Sugar, Flour, Salt  

**Sequence B (Customer B):**  
Bread, Butter, Cheese, Bananas, Yogurt, Orange Juice, Coffee, Sugar, Flour, Olive Oil, Salt  

---

## Algorithm
1. Create a DP table `dp[m+1][n+1]` where `dp[i][j]` represents the LCS length of `A[:i]` and `B[:j]`.
2. Recurrence:  
   - If `A[i-1] == B[j-1]`: `dp[i][j] = dp[i-1][j-1] + 1`  
   - Else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`
3. Fill the table and backtrack from `dp[m][n]` to reconstruct the LCS.

---

## Results

- **Length of LCS:** 9  
- **Longest Common Subsequence:**  
`['Bread', 'Butter', 'Cheese', 'Bananas', 'Yogurt', 'Coffee', 'Sugar', 'Flour', 'Salt']`

---

## Time Complexity
- Filling the table: O(m × n)  
- Backtracking: O(m + n)  
- **Overall:** O(m × n), which is polynomial, so the problem is in **P**.

