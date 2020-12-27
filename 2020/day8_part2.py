import copy
def main():

    # read in data
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day8_data.txt'
    with open(file_path, 'r') as f:
        info_list = f.readlines()
    
    # get all the nop and jump list that got run
    nop_list = []
    jmp_list = []
    exe_line_num = []
    i = 0
    while 0 <= i < len(info_list):
        line = info_list[i]
        if i in exe_line_num:
            break
        else:
            exe_line_num.append(i)
            commands = line.split(' ')
            if commands[0] == 'acc':
                i += 1
            if commands[0] == 'jmp':
                jmp_list.append(i)
                i += int(commands[1])
            if commands[0] == 'nop':
                nop_list.append(i)
                i += 1
    
    # brute-force changing each nop to jmp
    valid_nop = change_command(nop_list, info_list, 'jmp')
    valid_jmp = change_command(jmp_list, info_list, 'nop')
    if valid_nop:
        print('accumulator is {}'.format(valid_nop))
    else:
        if valid_jmp:
            print('accumulator is {}'.format(valid_jmp))
        else:
            print('No changes help!')

        
def change_command(command_list:list, info_list:list, new_command:str):
    k = 0
    new_list = info_list
    while not check_validity(new_list):
        if k < len(command_list):
            j = command_list[k]
            command_num = info_list[j].split(' ')[1]
            new_list = copy.deepcopy(info_list)
            new_list[j] = new_command + ' ' + str(command_num)
            k += 1
        else:
            return False
            break
    accumulator = check_validity(new_list)
    return accumulator


    
def check_validity(info_list:list):
    accumulator = 0
    i = 0
    exe_line_num = []
    while 0 <= i < len(info_list):
        line = info_list[i]
        if i in exe_line_num:
            return False
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
    return accumulator

if __name__ == '__main__':
    main()
