def main():
    # read in the strings
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day5_data.txt'
    with open(file_path, 'r') as f:
        info_list = f.readlines()
    
    bin_list = []
    for info in info_list:
        s = info.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
        bin_list.append(int(s, 2))
    
    bin_list = sorted(bin_list)
    current = bin_list[0]
    for i in bin_list:
        if i != current:
            print('Missing seat ID: {}'.format(current))
            return
        current += 1

if __name__ == '__main__':
    main()
