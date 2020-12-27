def main():

    # read in data
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day8_data.txt'
    with open(file_path, 'r') as f:
        info_list = f.readlines()
    
    accumulator = 0
    i = 0
    exe_line_num = []
    while 0 <= i < len(info_list):
        line = info_list[i]
        if i in exe_line_num:
            break
        else:
            exe_line_num.append(i)
            commands = line.split(' ')
            if commands[0] == 'acc':
                accumulator += int(commands[1])
                i += 1
            if commands[0] == 'jmp':
                i += int(commands[1])
            if commands[0] == 'nop':
                i += 1
    
    print('accumulator is {}'.format(accumulator))

if __name__ == '__main__':
    main()
