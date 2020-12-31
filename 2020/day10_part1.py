def main():
    # read in the data
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day10_data.txt'
    with open(file_path, 'r') as f:
        str_list = f.readlines()
    int_list = [int(item) for item in str_list]
    int_list.sort()
    
    # Calculate the difference
    diff_3 = 1
    diff_1 = 1
    for i in range(len(int_list)-1):
        diff = int_list[i+1] - int_list[i]
        if diff == 1:
            diff_1 += 1
        elif diff == 3:
            diff_3 += 1
    print('diff_1={}, and diff_3={}'.format(diff_1, diff_3))
    print('multiplication={}'.format(diff_1*diff_3))


if __name__ == '__main__':
    main()
