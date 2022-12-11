from collections import defaultdict

rules = []
with open('/Users/danielseal/git_local/AOC_2022/data/day11.txt') as f:
    for line in f.readlines():
        rules.append(line[:-1].strip())

monkeys = {}
for e, r in enumerate(rules):
    if r[:6] == 'Monkey':
        items = [int(i.strip()) for i in rules[e+1].split(':')[-1].strip().split(',')]
        ops = rules[e+2].split(':')[-1].split('= ')[-1].split('old ')[-1].split()
        test = (int(rules[e+3].split(':')[-1].split('by ')[-1]))
        outcome = [rules[e+4].split(':')[-1].split('monkey ')[-1].strip(), rules[e+5].split(':')[-1].split('monkey ')[-1].strip()]
        monkeys[r[7]] = [items, ops, test, outcome]

rounds = 0
num_rounds = 500 # 1000 for p2 
checker = defaultdict(int)
while rounds < num_rounds:  
    rounds += 1
    print(f'Round {rounds}....')
    for k, v in monkeys.items():
        checker[k] += len(v[0])  # add number of items to item checker count
        for item in v[0]:
            if v[1][0] == '-':
                if v[1][1] == 'old':
                    score = item - item
                else:
                    score = item - int(v[1][1])
            elif v[1][0] == '/':
                if v[1][1] == 'old':
                    score = item / item
                else:
                    score = item / int(v[1][1])
            elif v[1][0] == '+':
                if v[1][1] == 'old':
                    score = item + item
                else:
                    score = item + int(v[1][1])
            elif v[1][0] == '*':
                if v[1][1] == 'old':
                    score = item * item
                else:
                    score = item * int(v[1][1])

            # COMMENT OUT for p2
            # score = int(score / 3)  # applying relief
            t = True if score % v[2] == 0 else False # applying test 

            if t:
                monkeys[v[-1][0]][0].append(score)
            else:
                monkeys[v[-1][1]][0].append(score)

        monkeys[k][0] = []  # remove items from monkeys list

print(checker)
x1 = sorted([v for _, v in checker.items()])[::-1][:2][0]
x2 = sorted([v for _, v in checker.items()])[::-1][:2][1]

print(f'Part 1 Answer: {x1*x2}')


