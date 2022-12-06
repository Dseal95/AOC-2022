import numpy as np

map = []
instructions = []
with open('/Users/danielseal/git_local/AOC_2022/data/day5.txt', 'r') as f:
    for line in f.readlines():
        if line[:1] != 'm':
            pass
        else:
            tomove = line[:-1].split()[1]
            movefrom = str(int(line[:-1].split()[3])-1)
            moveto = str(int(line[:-1].split()[-1])-1)
            instructions.append([tomove, movefrom, moveto])
            
# board = [
#     ['   ', '[D]', '   '],
#     ['[N]', '[C]', '   '],
#     ['[Z]', '[M]', '[P]']
# ]
board = [
    ['[P]', '   ', '[C]', '   ', '   ', '[M]', '   ', '   ', '   '],
    ['[D]', '   ', '[P]', '[B]', '   ', '[V]', '[S]', '   ', '   '],
    ['[Q]', '[V]', '[R]', '[V]', '   ', '[G]', '[B]', '   ', '   '],
    ['[R]', '[W]', '[G]', '[J]', '   ', '[T]', '[M]', '   ', '[V]'],
    ['[V]', '[Q]', '[Q]', '[F]', '[C]', '[N]', '[V]', '   ', '[W]'],
    ['[B]', '[Z]', '[Z]', '[H]', '[L]', '[P]', '[L]', '[J]', '[N]'],
    ['[H]', '[D]', '[L]', '[D]', '[W]', '[R]', '[R]', '[P]', '[C]'],
    ['[F]', '[L]', '[H]', '[R]', '[Z]', '[J]', '[J]', '[D]', '[D]'],
]

mapped = {}
for e, i in enumerate(np.transpose(board)):
    mapped[str(e)] = [x for x in list(i) if x != '   ']

for inst in instructions:
    crates_to_move = [i for i in mapped[str(inst[1])]][:int(inst[0])]
    crates_from_list = [i for i in mapped[str(inst[1])][int(inst[0]): ]]
    moving_to_list = [i for i in mapped[str(inst[2])]]
    
    # COMMENT for 1 and 2
    # for c in crates_to_move:
    for c in crates_to_move[::-1]:
        moving_to_list.insert(0, c)

    # print(crates_from_list, crates_to_move, moving_to_list, crates_to_move[::-1])

    # update board
    mapped[inst[1]] = crates_from_list
    mapped[inst[2]] = moving_to_list

tops = []
for k, v in mapped.items():
    tops.append(v[0][1])

# answer 1
print(''.join(tops))
