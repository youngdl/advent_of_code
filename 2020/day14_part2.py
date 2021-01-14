import re
import itertools
import copy


def main():
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day14_data.txt'
    with open(file_path, 'r') as f:
        input_list = f.readlines()
    mask = None
    addr_value = {}
    pattern = re.compile('^mem\[(\d+)\] = (\d+)')
    for line in input_list:
        if line.startswith('mask'):
            mask = list(line.strip()[-36:])
        elif line.startswith('mem'):
            ismatch = pattern.match(line)
            addr, value = int(ismatch.group(1)), int(ismatch.group(2))
            bi_addr = list('{:036b}'.format(addr))
            for i in range(len(mask)):
                if mask[i] == '0':
                    continue
                elif mask[i] == '1':
                    bi_addr[i] = '1'
                elif mask[i] == 'X':
                    bi_addr[i] = 'X'
            mul_num = num_generator(bi_addr)
            for num in mul_num:
                addr_value[num] = value
    
    summary = sum(addr_value.values())
    print('The final result is {}'.format(summary))



def num_generator(bi_addr: list) -> list:
    result = []
    length = bi_addr.count('X')
    comb = list(itertools.product('01', repeat=length))
    for item in comb:
        new_list = copy.deepcopy(bi_addr)
        i = 0
        for index in range(len(bi_addr)):
            if bi_addr[index] == 'X':
                new_list[index] = item[i]
                i += 1
        temp = ''.join(new_list)
        new_num = int(temp, 2)
        result.append(new_num)
    return result


if __name__ == '__main__':
    main()
