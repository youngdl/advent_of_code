import copy
from typing import Set, Tuple

def main():
    # read in data
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day17_data.txt'
    with open(file_path, 'r') as f:
        input_list = f.readlines()
    d0 = len(input_list)
    cycle = 6
    
    # generate the initial coordinate set from the original data 
    pattern_list = [list(item.strip()) for item in input_list]
    coor_set = Set[Tuple[int, int, int, int]]
    active_set: coor_set = set()
    for y in range(len(pattern_list)):
        for x in range(len(pattern_list[y])):
            if pattern_list[y][x] == '#':
                active_set.add((0,0,y,x))  #coordinates are in order of w,z,y,x 
    
    # loop over all dimension to flip the state
    xy_start = 0 - cycle
    xy_end = d0-1 + cycle
    z_start = 0 - cycle
    z_end = 0 + cycle
    w_start = 0 - cycle
    w_end = 0 + cycle
    
    # abstract the function of flipping state for one cycle 
    def flip_state_one_cycle(active):
        a_set: coor_set = set()
        for w in range(w_start, w_end+1):
            for z in range(z_start, z_end+1):
                for y in range(xy_start, xy_end+1):
                    for x in range(xy_start, xy_end+1):
                        if _isvalid((w,z,y,x), active):
                            a_set.add((w,z,y,x))
        return a_set
    
    # Flipping state over given cycle
    for c in range(cycle):
        temp_set = flip_state_one_cycle(active_set)
        active_set = temp_set
        # print('The new set is \n{}'.format(active_set))
        print('The lenth of the new set is {}'.format(len(active_set)))
        print('-----'*20)

# Function to evaluate the status of given data point
def _isvalid(coordinate, active_set):
    w, z, y, x = coordinate
    counts = 0
    for n in range(w-1, w+2):
        for i in range(z-1, z+2):
            for j in range(y-1, y+2):
                for k in range(x-1, x+2):
                    if (n,i,j,k) != (w,z,y,x):
                        if (n,i,j,k) in active_set:
                            counts += 1
    if (w,z,y,x) in active_set: 
        if (counts == 2 or counts == 3):
            return True
    else:
        if counts == 3:
            return True
    return False        


if __name__ == '__main__':
    main()
