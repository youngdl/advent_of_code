# read in data and generate a list of all lines
file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day3_data.txt'
with open(file_path, 'r') as f:
    lines = f.readlines()

# Change the symbol map to a digital map
digital_map = []
for line in lines:
    updated_line = []
    for char in list(line[:-1]):
        if char == '.':
            updated_line.append(0)
        else:
            updated_line.append(1)
    digital_map.append(updated_line)


def tree_numbers(digital_map:list, slope:tuple):

    # extend horizontal direction
    x_stepsize = slope[0] 
    y_stepsize = slope[1] 
    x_dim = len(digital_map[0])
    y_dim = len(digital_map)
    steps = (y_dim-1)//y_stepsize
    for line in digital_map:
        while len(line) < x_stepsize * steps + 1:
            line.extend(line)

    # count the number of trees that encountered
    i, j = 0, 0
    tree_num = 0
    for k in range(steps+1):
        tree_num = tree_num + digital_map[j][i]
        i += x_stepsize
        j += y_stepsize 
    print('The number of trees that has been passed is {}'.format(tree_num))
    return tree_num

route1 = tree_numbers(digital_map, (1, 1))
route2 = tree_numbers(digital_map, (3, 1))
route3 = tree_numbers(digital_map, (5, 1))
route4 = tree_numbers(digital_map, (7, 1))
route5 = tree_numbers(digital_map, (1, 2))
mul = route1 * route2 * route3 * route4 * route5  
print(mul)
