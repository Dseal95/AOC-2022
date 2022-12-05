import numpy as np 

count = 0
count2 = 0

with open('/Users/danielseal/git_local/AOC_2022/data/day4.txt', 'r') as f:
    for line in f.readlines():
        L = np.arange(int(line[:-1].split(',')[0].split('-')[0]), int(line[:-1].split(',')[0].split('-')[-1])+1)
        R = np.arange(int(line[:-1].split(',')[-1].split('-')[0]), int(line[:-1].split(',')[-1].split('-')[-1])+1)

        ArrL = np.array([0]*int(max(max(L), max(R))+1))
        ArrR = np.array([0]*int(max(max(L), max(R))+1))
        
        for i in L:
            ArrL[i] += 1
        for i in R:
            ArrR[i] += 1
        ArrSum = ArrL + ArrR
        
        if len(ArrSum[ArrSum >= 2]) >= min(len(L), len(R)):
            count += 1
        if len(ArrSum[ArrSum >= 2]) > 0:
            count2 += 1

# Answer 1
print(f"Part 1 Answer = {count}")
# Answer 2
print(f"Part 2 Answer = {count2}")