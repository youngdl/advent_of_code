def main():
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day11_data.txt'
    with open(file_path, 'r') as f:
        str_list = f.readlines()
    input_list = []
    for line in str_list:
        line = line.strip('\n')
        input_list.append(line)

    row_num = len(input_list)
    col_num = len(input_list[0])
    new_list = [list(item) for item in input_list]
    old_list = None
    # import pdb; pdb.set_trace()

    while new_list != old_list:
        old_list = [list(item) for item in new_list]
        for row in range(row_num):
            for col in range(col_num):
                new_list[row][col] = update((row,col), old_list)
        print_seats(new_list)

    sum_num = 0
    for row in range(row_num):
        for col in range(col_num):
            if new_list[row][col] == '#':
                sum_num += 1
    print('sum_num is {}'.format(sum_num))


def print_seats(array: list) -> None:
    for item in array:
        print(''.join(item))
    print('-' * 80)
    

def update(position:tuple, array:list) -> str:
    row, col = position
    current_element = array[row][col]
    
    def occupied_neibor() -> int:
        occupied = 0
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if i < 0 or j < 0 or i >= len(array) or j >= len(array[0]) or (i == row and j == col):
                    pass
                else:
                    if array[i][j] == '#':
                        occupied += 1
        return occupied

    if current_element == '.':
        return '.'
    elif current_element == 'L':
        if occupied_neibor() == 0:
            return '#'
        else:
            return 'L'
    elif current_element == '#':
        if occupied_neibor() >= 4:
            return 'L'
        else:
            return '#'


if __name__ == '__main__':
    main()
