import copy
from typing import Set, Tuple

def main():
    # read in data
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day17_data.txt'
    with open(file_path, 'r') as f:
        input_list = f.readlines()
    d0 = len(input_list)
    cycle = 6
    pattern_list = [list(item.strip()) for item in input_list]
    coor_set = Set[Tuple[int, int, int]]
    active_set: coor_set = set()
    for y in range(len(pattern_list)):
        for x in range(len(pattern_list[y])):
            if pattern_list[y][x] == '#':
                active_set.add((0,y,x))
    
    xy_start = 0 - cycle
    xy_end = d0-1 + cycle
    z_start = 0 - cycle
    z_end = 0 + cycle
    for c in range(cycle):
        temp_active_set: coor_set = set()
        for z in range(z_start, z_end+1):
            for y in range(xy_start, xy_end+1):
                for x in range(xy_start, xy_end+1):
                    if _isvalid((z, y, x), active_set):
                        temp_active_set.add((z, y, x))
        active_set = temp_active_set
    print('The result is {}'.format(len(active_set)))   
             
def _isvalid(coordinate, active_set):
    z, y, x = coordinate
    counts = 0
    for i in range(z-1, z+2):
        for j in range(y-1, y+2):
            for k in range(x-1, x+2):
                if (i,j,k) != (z,y,x):
                    if (i,j,k) in active_set:
                        counts += 1
    
    if (z,y,x) in active_set:
        if counts == 2 or counts == 3:
            return True
        else:
            return False
    else:
        if counts == 3:
            return True
        else:
            return False

if __name__ == '__main__':
    main()
