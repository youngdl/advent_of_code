import copy

def main():
    # read in data
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day17_data.txt'
    with open(file_path, 'r') as f:
        input_list = f.readlines()
    d0 = len(input_list)
    pattern_list = [list(item.strip()) for item in input_list]
    
    # create a zero data _array to operate with
    cycle = 6
    z_dimension = 1 + 2 * (cycle+1)
    x_dimension = d0 + 2 * (cycle+1)
    x_list = [0] * x_dimension
    xy_array = [list(x_list) for _ in range(x_dimension)]
    z_array = []
    for i in range(z_dimension):
        z_array.append(copy.deepcopy(xy_array))

    # Put the original pattern into the new _array
    for row in range(d0):
        for col in range(d0):
            if pattern_list[row][col] == '#':
                z = (z_dimension -1) // 2
                x = (x_dimension -1) // 2 - (d0 - 1) // 2 + col
                y = (x_dimension -1) // 2 - (d0 - 1) // 2 + row
                z_array[z][y][x] = 1

    result = 0
    for a in range(z_dimension):
        for j in range(x_dimension):
            for k in range(x_dimension):
                result += z_array[a][j][k]
    print('result is {}'.format(result))

    # Flip status one cycle after another
    for i in range(1, cycle+1):
        z_start = (z_dimension -1) // 2 - i
        z_end = (z_dimension -1) // 2 + i
        x_start = (x_dimension -1) // 2 - (d0 - 1) // 2 - i - 1
        x_end = (x_dimension -1) // 2 + (d0 - 1) // 2 + i + 1
        y_start = (x_dimension -1) // 2 - (d0 - 1) // 2 - i - 1
        y_end = (x_dimension -1) // 2 + (d0 - 1) // 2 + i + 1
        update_array = copy.deepcopy(z_array)
        # for i in range(z_dimension):
        #     for j in range(x_dimension):
        #         for k in range(x_dimension):
        for i in range(z_start, z_end+1):
            for j in range(y_start, y_end+1):
                for k in range(x_start, x_end+1):
                    if _isactive(z_array, i, j, k):
                        update_array[i][j][k] = 1
                    else:
                        update_array[i][j][k] = 0
        z_array = update_array
        # print_state(z_array, z_start, z_end)

    # Loop through all elements in z_array and get the sum_num as active cube num
        result = 0
        for a in range(z_dimension):
            for j in range(x_dimension):
                for k in range(x_dimension):
                    result += z_array[a][j][k]
        print('result is {}'.format(result))



def print_state(data, z_start, z_end) -> None:
    for i in range(z_start, z_end+1):
        print('z={}'.format(i))
        for row in data[i]:
            print(''.join(str(e) for e in row))
        print()

def _isactive(_array,i,j,k) -> bool:
    sum_num = 0
    for z in range(i-1, i+2):
        for y in range(j-1, j+2):
            for x in range(k-1, k+2):
                if (x, y, z) != (k, j, i):
                    sum_num += _array[z][y][x]
    if _array[i][j][k] == 1:
        if sum_num == 2 or sum_num == 3:
            return True
        else:
            return False
    elif _array[i][j][k] == 0:
        if sum_num == 3:
            return True
        else:
            return False


if __name__ == '__main__':
    main()
