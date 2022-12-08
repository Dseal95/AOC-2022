from collections import defaultdict

cmds = []
with open('/Users/danielseal/git_local/AOC_2022/data/day7.txt') as f:
    for line in f.readlines():
        cmds.append(line[:-1].split())

path_sizes = defaultdict(int)
path = []
for cmd in cmds:
    print('1')
    print(cmd)
    if cmd[1] == 'cd':
        if cmd[2] == '..':
            path.pop()  # remove last 
        else:
            path.append(cmd[2])
    elif (cmd[1] == 'ls') | (cmd[0] == 'dir'):
        pass  # stay at level, do nothing
    else:
        # file
        size = int(cmd[0])
        for i in range(1, len(path)+1):
            # add all parents
            path_sizes['/'.join(path[:i])] += size

# part 1 
p1 = 0
for k, v in path_sizes.items():
    if v <= 100000:
        p1+=v

print(f'Part 1 Answer: {p1}')

# part 2 
max_size = 70000000
my_max_size_allowed = max_size - 30000000
curr_size = path_sizes['/']
possible = []
for k, v in path_sizes.items():
    if v >= (curr_size - my_max_size_allowed):
        possible.append(v)

print(f'Part 1 Answer: {min(possible)}')