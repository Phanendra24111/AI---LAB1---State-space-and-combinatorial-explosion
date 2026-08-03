# Lab 1 - Water Jug Problem (State Space)

## Problem Statement

Jug X holds 4 litres, Jug Y holds 3 litres. Both are unmarked and start empty.
Water is unlimited. There are 6 operations allowed - Fill X, Fill Y, Empty X,
Empty Y, Pour X into Y, Pour Y into X.

A state is written as (x, y) - the amount of water in X and in Y.
The task is to start from (0,0), find all states reachable, and see how the
number of new states grows level by level. A simple tree would predict
6, 36, 216, 1296... new states, but that's not what actually happens.

## My Approach

I represented each jug reading as a state (x, y) and wrote a successors()
function that lists all 6 states reachable by one move. I explored outward
from (0,0) level by level, using a `seen` set to skip any state I'd already
found, so I never re-count a repeated state. This turned an exploding
6-branch tree into the true, much smaller state graph - only 14 of the 20
possible (x, y) pairs are actually reachable, since every move forces at
least one jug to become fully empty or fully full.

## Output

```
Level 1 ->  2 new states: [(0, 3), (4, 0)]
Level 2 ->  3 new states: [(1, 3), (3, 0), (4, 3)]
Level 3 ->  2 new states: [(1, 0), (3, 3)]
Level 4 ->  2 new states: [(0, 1), (4, 2)]
Level 5 ->  2 new states: [(0, 2), (4, 1)]
   *** GOAL: 2L in X at level 6 ***
Level 6 ->  2 new states: [(2, 0), (2, 3)]
Level 7 ->  0 new states: []
Total states found: 14
```

## What I found

Tree formula says levels should have 6, 36, 216, 1296 new states.
Actual program only finds 2, 3, 2, 2, 2, 2, 0 new states - total 14, not
thousands.

The reason is this one line:

```python
if ns not in seen:
```

Without it, the program would keep re-counting states it already visited,
and the numbers would explode like the tree formula. With it, once a state
is seen, it's never added again - so the search stops growing once it runs
out of new places to go.

Out of 20 possible (x,y) pairs (5 values of x times 4 values of y), only
14 are reachable. The 6 that are missing - (1,1) (1,2) (2,1) (2,2) (3,1)
(3,2) - can never happen because every operation always leaves at least
one jug either completely empty or completely full. So both jugs can
never be "half full" at the same time.

## Files
- water_jug_lab1.py - the code
- notes - my handwritten notes for this lab

## How to run
```
python3 water_jug_lab1.py
```
