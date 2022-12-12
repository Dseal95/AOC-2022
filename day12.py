from collections import deque

grid = []
with open('/Users/danielseal/git_local/AOC_2022/data/day12.txt') as f:
    for line in f.readlines():
        grid.append(list(line[:-1]))

imax = len(grid)
jmax = len(grid[0])
visited = deque()

# convert all tile to numbers once know S
ngrid = [[0 for _ in range(jmax)] for _ in range(imax)]
for i in range(imax):
    for j in range(jmax):
        if grid[i][j] == 'S':
            ngrid[i][j] = ord('a') - 96
        elif grid[i][j] == 'E':
            ngrid[i][j] = ord('z') - 96
        else:
            ngrid[i][j] = ord(grid[i][j]) - 96

for i in range(imax):
    for j in range(jmax):
        # if ngrid[i][j] == 1:
        #     visited.append(((i, j), 0))
        if grid[i][j] == 'S':
            visited.append(((i, j), 0)) # add starting position to visited

path = set()
while visited:
    (i, j), cost = visited.popleft()
    # print(f'Start: grid[{i}][{j}] = {grid[i][j]}, cost={cost}')
    if (i, j) in path:
        continue # already been here and taken same or less cost, do nothing
    path.add((i, j))

    if grid[i][j] == 'E':
        print(cost)
        assert False 
    
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ii = i + dx
        jj = j + dy
        
        if (0<=ii<imax) and (0<=jj<jmax) and (ngrid[ii][jj] <= (ngrid[i][j] + 1)):
            # print(f'SEARCH: grid[{ii}][{jj}] = {grid[ii][jj]}, cost={cost+1}')
            visited.append(((ii, jj), cost+1))



    