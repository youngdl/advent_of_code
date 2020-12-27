import copy


def main():
    # read in data
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day8_data.txt'
    with open(file_path, 'r') as f:
        info_list = f.readlines()
    
    change_list = get_change_list(info_list)
    # brute-force changing each nop to jmp
    valid = change_command(change_list, info_list)
    if valid:
        print('accumulator is {}'.format(valid))
    else:
        print('No changes help!')


def get_change_list(info_list: list):
    # get all the nop and jump list that got run
    change_list = []
    exe_line_num = set()
    i = 0
    while 0 <= i < len(info_list):
        line = info_list[i]
        if i in exe_line_num:
            break

        exe_line_num.add(i)
        commands = line.split(' ')
        if commands[0] == 'acc':
            i += 1
        if commands[0] == 'jmp':
            change_list.append(i)
            i += int(commands[1])
        if commands[0] == 'nop':
            change_list.append(i)
            i += 1
    return change_list


def change_command(change_list: list, info_list: list):
    for j in change_list:
        new_list = copy.deepcopy(info_list)
        if new_list[j].startswith('nop'):
            new_list[j] = new_list[j].replace('nop', 'jmp')
        elif new_list[j].startswith('jmp'):
            new_list[j] = new_list[j].replace('jmp', 'nop')
        
        valid = check_validity(new_list)
        if valid:
            return valid
    return False

    
def check_validity(info_list: list):
    accumulator = 0
    i = 0
    exe_line_num = []

    while 0 <= i < len(info_list):
        line = info_list[i]
        if i in exe_line_num:
            return False

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
