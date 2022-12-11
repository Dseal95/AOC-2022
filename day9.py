def generate_NN(i, j):
    coords = [(i, j), (i+1, j), (i-1, j), (i, j+1), (i, j-1), (i-1, j-1), (i+1, j-1), (i-1, j+1), (i+1, j+1)]
    
    return coords

def next_position(move, initial_position):
    dist = move[-1]

    i, j = initial_position[0], initial_position[-1]

    if move[0] == "R":
        new_position = (i, (j+dist))
    elif move[0] == "L":
        new_position = (i, (j-dist))
    elif move[0] == "U":
        new_position = ((i-dist), j)
    elif move[0] == "D":
        new_position = ((i+dist), j)
    else:
        raise ValueError('Direction not handled.')    
    
    return new_position

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

    return coords


if '__main__'== __name__:
    moves = []
    with open('/Users/danielseal/git_local/AOC_2022/data/day9.txt') as f:
        for line in f.readlines():
            moves.append([line[:-1].split()[0], int(line[:-1].split()[-1])])

    s = (0, 0)  # initial position 
    visitedT = [s]
    visitedH = [s]
    for m in moves:
        H_new = next_position(move=m, initial_position=visitedH[-1])
        
        H_coords = generate_coordinates_between_two_points(p1=visitedH[-1], p2=H_new) + [H_new]
        for s_ in H_coords:
            visitedH.append(s_)
        
        for p in H_coords:
            if visitedT[-1] in generate_NN(i=p[0], j=p[-1]):
                # adjacent, do nothing
                pass
            else:
                # not adjacent 
                H_NN = generate_NN(i=p[0], j=p[-1])
                T_NN = generate_NN(i=visitedT[-1][0], j=visitedT[-1][-1])
                visitedT.append([c for c in [i for i in T_NN if i in H_NN] if c in H_coords][0])
    
    print(f'Part 1 Answer: {len(set(visitedT))}')

            
    

