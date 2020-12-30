def main():
    # read in number list
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day9_data.txt'
    with open(file_path, 'r') as f:
        str_list = f.readlines()
    int_list = [int(item) for item in str_list]

    for i in range(25, len(int_list)):
        if int_list[i] not in sum_generator(int_list, (i-25, i-1)):
            print('The {}th number is {} and it is invalid'.format(i,int_list[i]))
            break
    if i == len(int_list)-1:
        print('All numbers are valid')


def sum_generator(num_list: list, location: tuple) -> set:
    return_set = set()
    start = location[0]
    end = location[1]
    for i in range(start, end):
        for j in range(i+1, end+1):
            if num_list[j] != num_list[i]:
                summary = num_list[i] + num_list[j]
                return_set.add(summary)
    return return_set


if __name__ == '__main__':
    main()
