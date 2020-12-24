def main():

    # read in the strings
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day5_data.txt'
    with open(file_path, 'r') as f:
        info_list = f.readlines()
    
    # Check the seat position and get the max
    id_list=[]
    for line in info_list:
        seat_row_start, seat_row_end = 0, 127
        seat_col_start, seat_col_end = 0, 7
        for i in range(7):
            if line[i] == 'F':
                seat_row_end = (seat_row_end + seat_row_start) // 2
            else:
                seat_row_start = (seat_row_end + seat_row_start) // 2 + 1
        
        for j in range(7,10):
            if line[j] == 'L':
                seat_col_end = (seat_col_start + seat_col_end) // 2 
            else:
                seat_col_start = (seat_col_start + seat_col_end) // 2 + 1
        seat_id = seat_row_end * 8 + seat_col_end
        id_list.append(seat_id)

    max_id = max(id_list)
    print(len(id_list))
    print(max_id)


if __name__ == '__main__':
    main()
