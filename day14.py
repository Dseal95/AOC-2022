def generate_coordinates_between_two_points(p1, p2):
    if p1[0] == p2[0]:
        # moved y-direction
        if p1[-1] > p2[-1]:
            # decreasing 
            coords = [(p1[0], j) for j in range(p1[-1], p2[-1], -1)]
        else:
            # increasing
            coords = [(p1[0], j) for j in range(p1[-1], p2[-1], 1)]

    elif p1[-1] == p2[-1]:
        # moved x-direction
        if p1[0] > p2[0]:
            # decreasing 
            coords = [(i, p1[-1]) for i in range(p1[0], p2[0], -1)]
        else:
            # increasing
            coords = [(i, p1[-1]) for i in range(p1[0], p2[0], 1)]

    return coords + [p2]


def down(c):
    return (c[0], c[1]+1)


def downleft(c):
    return (c[0]-1, c[1]+1)


def downright(c):
    return (c[0]+1, c[1]+1)


def move(c, moved, rocks):    
    global depth
    if c[1] > depth:
        return False

    if len(set(moved)) == 3:
        rocks.append(c)  # sand becomes equivalent to a rock 
        return c

    if (down(c) not in rocks):
        return move(down(c), moved, rocks)
        
    elif (down(c) in rocks) and (downleft(c) not in rocks):
        return move(downleft(c), moved, rocks)

    elif (downleft(c) in rocks) and (downright(c) not in rocks):
        return move(downright(c), moved, rocks)
    
    else:
        moved.append('dr')
        moved.append('d')
        moved.append('dl')
        return move(c, moved, rocks)


if '__main__' == __name__:
    rocks = []
    with open('/Users/danielseal/git_local/AOC_2022/data/day14.txt') as f:
        for line in f:
            cs = [(int(i.split(',')[0]), int(i.split(',')[-1]))  for i in line[:-1].split(' -> ')]
            for i in range(len(cs)-1):
                for coord in generate_coordinates_between_two_points(p1=cs[i], p2=cs[i+1]):
                    if coord not in rocks:
                        rocks.append(coord)

    
    depth = max([r[-1] for r in rocks])
    # # uncomment for p2  
    # depth += 2

    S = (500, 0)
    sands = []
    result = True
    i = 0
    while result:
        sand = move(S, moved=[], rocks=rocks)
        sands.append(sand)
        result = False if sand is False else True
        i+=1
        
    print(f'Part 1 Answer = {i-1}')


