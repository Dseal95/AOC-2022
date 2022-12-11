operations = []
with open('/Users/danielseal/git_local/AOC_2022/data/day10.txt') as f:
        for line in f.readlines():
            operations.append(line[:-1].split())

cycle = 1
X = 1
program = {}
modified_operations = []

for cmd in operations: 
    if cmd[0] == 'noop':
        modified_operations.append(0)
    elif cmd[0] == 'addx':
        modified_operations.append(0)
        modified_operations.append(int(cmd[-1]))

for i in modified_operations:
    cycle+=1
    X+=i
    program[str(cycle)] = cycle*X

# part 1 
print(f"Part 1 Answer = {program['20'] + program['60'] + program['100'] + program['140'] + program['180'] + program['220']}")
    
# Part 2
print('Part 2 Answer...')
s = 0
cycle = 1
X = 1
for j in range(int(len(modified_operations)/40)):    
    T = []
    for e, k in enumerate(range(s, s+40)):
        T.append("#" if e in [X-1, X, X+1] else ".")
        cycle+=1
        X+=modified_operations[k]
        
    print(''.join(T))
    s+=40

     