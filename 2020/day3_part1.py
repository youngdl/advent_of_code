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

# extend horizontal direction 
x_dim = len(digital_map[0])
y_dim = len(digital_map)
steps = (y_dim-1)//1
for line in digital_map:
    while len(line) < 3 * steps + 1:
        line.extend(line)

# count the number of trees that encountered
i, j = 0, 0
tree_num = 0
for k in range(y_dim):
    tree_num = tree_num + digital_map[j][i]
    i += 3
    j += 1 
print('The number of trees that has been passed is {}'.format(tree_num))
