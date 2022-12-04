priorities = []
i = 1
group = []
G = []
with open('/Users/danielseal/git_local/AOC_2022/data/day3.txt', 'r') as f:
    for line in f.readlines():
        group.append(list(line[:-1]))
        L = list(line[:-1])[:len(list(line[:-1]))//2]
        R = list(line[:-1])[len(list(line[:-1]))//2:]
        priorities.append(list(set([i for i in L if i in R]))[0])

        if i % 3 == 0:
            G.append(list(set([i for i in group[0] if i in list(set([e for e in group[1] if i in group[2]]))]))[0])
            group = []
        i+=1

S = []
for p in priorities:
    if p.isupper():
        S.append((ord(p.lower())-96) + 26)
    else:
        S.append((ord(p.lower())-96))

# answer 1
print(f'Answer 1 = {sum(S)}')

S2 = []
for l in G:
    if l.isupper():
        S2.append((ord(l.lower())-96) + 26)
    else:
        S2.append((ord(l.lower())-96))

# answer 2
print(f'Answer 2 = {sum(S2)}')
