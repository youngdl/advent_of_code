def main():
    # read in number list
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day9_data.txt'
    with open(file_path, 'r') as f:
        str_list = f.readlines()
    int_list = [int(item) for item in str_list]
    a = 20874512
    for i in range(len(int_list)-1):
        summary = int_list[i]
        k = i+1
        while summary < a:
            summary += int_list[k]
            k += 1
            if k >= len(int_list):
                break
        if summary == a:
            print('sum is from {}th number{}, to {}th number{}'.format(i, int_list[i], k, int_list[k]))
            break

    max_num = max(int_list[i:k+1])
    min_num = min(int_list[i:k+1])
    sum_num = max_num + min_num
    print('Max is {}, min is {}, and the sum is {}'.format(max_num, min_num, sum_num))


if __name__ == '__main__':
    main()
