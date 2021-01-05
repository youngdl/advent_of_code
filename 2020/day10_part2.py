def main():
    # read in the data
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day10_data.txt'
    with open(file_path, 'r') as f:
        str_list = f.readlines()
    int_list = [int(item) for item in str_list]
    max_num = max(int_list)
    
    result_dic = {}
    def num_con(n:int, adp_list:list) -> int:
        #function to calculated given certain adapter in a list of adapters, how many ways to connect it to the outlet(0 rating)
        if n in result_dic.keys():
            return result_dic[n]
        if n == 0:
            return 1
        if n not in adp_list:
            return 0

        sum_num = 0
        for k in [1,2,3]:
            temp = num_con(n-k, adp_list)
            result_dic[n-k] = temp
            sum_num += temp
        
        return sum_num

    print('ways of connection is {}'.format(num_con(max_num, int_list)))

if __name__ == '__main__':
    main()
