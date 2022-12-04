scores = {"['A', 'X']": 3,
          "['A', 'Y']": 6,
          "['A', 'Z']": 0,
          "['B', 'X']": 0,
          "['B', 'Y']": 3,
          "['B', 'Z']": 6,
          "['C', 'X']": 6,
          "['C', 'Y']": 0,
          "['C', 'Z']": 3}

mapping  = {"['A', 'X']": 'Z',
            "['A', 'Y']": 'X',
            "['A', 'Z']": 'Y',
            "['B', 'X']": 'X',
            "['B', 'Y']": 'Y',
            "['B', 'Z']": 'Z',
            "['C', 'X']": 'Y',
            "['C', 'Y']": 'Z',
            "['C', 'Z']": 'X'}

shapes = {'X': 1, 'Y': 2, 'Z': 3}

results = []
with open('/Users/danielseal/git_local/AOC_2022/data/day2.txt', 'r') as f:
    for line in f.readlines()[:-1]:
        game = [line[:-1].split()[0], mapping[str(line[:-1].split())]]
        results.append((scores[str(game)] + shapes[game[-1]]))

# answer 1 + 2
print(sum(results))