from functools import cmp_to_key

def compare(L, R):
    # print(f'compare(L={L}, R={R})')
    if isinstance(L, int) and isinstance(R,int):
        # comparing integers 
        if L < R:
            return 1
        elif L == R:
            return 0
        else:
            # L > R
            return -1
    elif isinstance(L, list) and isinstance(R, list):
        # comparing list and int
        i = 0
        while (i < len(L)) and (i < len(R)):
            result = compare(L[i], R[i])
            if result == 1:
                # ordered
                return 1
            if result == -1:
                # not ordered
                return -1
            i += 1
        
        if i == len(L) and i < len(R):
            # ordered
            return 1
        elif i==len(R) and i<len(L):
            # not ordered
            return -1
        else:
            return 0

    elif isinstance(L, int) and isinstance(R, list):
        return compare([L], R)
    
    else:
        return compare(L, [R])

 
if '__main__' == __name__:
    P = []
    with open('/Users/danielseal/git_local/AOC_2022/data/day13.txt') as f:
        for line in f.readlines():
            if line != '\n':
                P.append(line[:-1])
    
    # Part 1:
    Ls = []
    Rs = []
    for i in range(0, len(P), 2):
       Ls.append(P[i:i+2][0])
       Rs.append(P[i:i+2][-1])
      
    correct_order = 0
    for e, packets in enumerate(list(zip(Ls, Rs))):
        res = compare(L=eval(packets[0]), R=eval(packets[-1]))
        if res == 1:
            correct_order+=(e+res)

    print(f'Part 1 Answer = {correct_order}')

    # part 2 
    packets = [eval(i) for i in P]

    # add 2 packets 
    packets.append(eval('[[2]]'))
    packets.append(eval('[[6]]'))
    packets = sorted(packets, key=cmp_to_key(lambda L, R: compare(L, R)), reverse=True)

    correct_order2 = 1
    for e, p in enumerate(packets):
        if p==eval('[[2]]') or p==eval('[[6]]'):
            correct_order2 *= e+1
    
    print(f'Part 2 Answer = {correct_order2}')


