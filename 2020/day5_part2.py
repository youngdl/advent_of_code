def find_seat_list():

    # read in the strings
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day5_data.txt'
    with open(file_path, 'r') as f:
        info_list = f.readlines()
    
    # Check the seat position and get the max
    seat_list=[]
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
        seat = (seat_row_start, seat_col_start)
        seat_list.append(seat)
    return(seat_list)

def main():
    temp_list = []
    for i in range(128):
        temp_list.append([0] * 8)
    seat_list = find_seat_list()
    for seat in seat_list:
        row = seat[0]
        col = seat[1]
        temp_list[row][col] = 1
    for i in range(1, len(temp_list)):
        for j in range(len(temp_list[i])):
            if temp_list[i][j] == 0 and temp_list[i-1][j] != 0 and temp_list[i+1][j] != 0:
                ID = 8 * i + j
                print('Seat founded at {}'.format((i,j)))  
                print('ID is:{}'.format(ID))

if __name__ == '__main__':
    main()
