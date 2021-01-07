def main():
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day11_data.txt'
    with open(file_path, 'r') as f:
        str_list = f.readlines()
    input_list = [list(line.strip('\n')) for line in str_list]

    row_num = len(input_list)
    col_num = len(input_list[0])
    new_list = [list(item) for item in input_list]
    old_list = None

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

        def check_seat(direction:tuple) -> str:
            xstep = direction[0]
            ystep = direction[1]
            seat = ''
            k = 1
            while seat == '.' or seat == '':
                if row + k * ystep >= len(array) or col + k * xstep >= len(array[0]) or row + k * ystep < 0 or col + k * xstep < 0:
                    break
                x_coord = col + k * xstep
                y_coord = row + k * ystep
                seat = array[y_coord][x_coord]
                k += 1
            return seat
        
        neibor_list = [
                       check_seat((0, -1)),
                       check_seat((1, -1)),
                       check_seat((1, 0)),
                       check_seat((1, 1)),
                       check_seat((0, 1)),
                       check_seat((-1, 1)),
                       check_seat((-1, 0)),
                       check_seat((-1, -1))
                       ]
        for item in neibor_list:
            if item == '#':
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
        if occupied_neibor() >= 5:
            return 'L'
        else:
            return '#'


if __name__ == '__main__':
    main()
