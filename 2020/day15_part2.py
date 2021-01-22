def main():

    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day15_data.txt'
    with open(file_path, 'r') as f:
        start_number = [int(i) for i in f.read().strip().split(',')]
    
    turn_dic = {}
    c = len(start_number)
    last_value = 0
    for i in range(c):
        turn_dic[start_number[i]] = i
    print(turn_dic)
    k = c+1
    while k < 30000000:
        if last_value not in turn_dic:
            turn_dic[last_value] = k-1
            last_value = 0
        else:
            temp = last_value
            last_value = k-1-turn_dic[last_value]
            turn_dic[temp] = k-1
        k += 1
        # print(last_value)
    print(last_value)


if __name__ == '__main__':
    main()
