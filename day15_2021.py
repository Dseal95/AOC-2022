from queue import PriorityQueue
import numpy as np 

grid = []
with open('/Users/danielseal/git_local/AOC_2021/data/day15.txt') as f:
    for line in f.readlines():
        grid.append([int(i) for i in list(line[:-1])])

# for i in grid:
#     print(i)

S = (0, (0, 0))
Q = PriorityQueue()
Q.put(S)
visited= {(0, 0)}
imax = len(grid)
jmax = len(grid[0])

while True:
    cost, (i, j) = Q.get()
    if (i==imax-1) and (j==jmax-1):
        print(cost)
        break
    for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ii = i + di
        jj = j + dj
        if (0<=ii<imax) and (0<=jj<jmax):
            if (ii, jj) not in visited:
                visited.add((ii, jj)) 
                Q.put((cost + grid[ii][jj], (ii, jj)))