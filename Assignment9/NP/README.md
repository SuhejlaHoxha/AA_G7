# Job Shop Scheduling Problem (JSSP) - Brute Force Solution

## Description
This project demonstrates solving a small instance of the Job Shop Scheduling Problem (JSSP) using brute force. JSSP is NP-hard, where multiple jobs must be scheduled on multiple machines minimizing the total completion time (makespan) while respecting job order and machine constraints.

## Problem Instance
- 4 Jobs (J1, J2, J3, J4)
- 3 Machines (M1, M2, M3)
- Each job has a sequence of tasks: (Machine, Processing Time)

## Solution Approach
- All permutations of jobs are evaluated.
- For each permutation, tasks are scheduled respecting:
  - Machine availability
  - Job task order
- Makespan is calculated, and the permutation with minimum makespan is selected.

## Code
- Implemented in Python using `itertools.permutations`.
- Calculates the optimal job sequence and corresponding makespan.

## Usage
1. Run `python job_shop_scheduling.py`
2. Output shows:
   - Optimal job sequence
   - Minimum makespan

## Complexity
- Brute force: O(n!) for n jobs (feasible only for small instances)
- NP-hard problem: For large n, heuristic or metaheuristic algorithms are recommended.

