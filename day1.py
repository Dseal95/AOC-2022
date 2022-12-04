E = {}
i = 0
calories = []
with open('/Users/danielseal/git_local/AOC_2022/data/day1.txt') as f:
    for line in f.readlines() + ['']:
        if line[:-1] != '':
            calories.append(line[:-1])
        if line[:-1] == '':
            E[i] = sum([int(i) for i in calories])
            calories = []
            i+=1

# answer 1   
print(max([v for _, v in E.items()]))
# answer 2
print(sum(sorted([v for _, v in E.items()])[::-1][:3]))