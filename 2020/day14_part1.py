import re

def main():
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day14_data.txt'
    with open(file_path, 'r') as f:
        input = f.read()
    input_list = input.split('\nmask = ')
    # print('input_list = {}'.format(input_list))

    pattern = re.compile('^mem\[(\d+)\] = (\d+)')
    element_dict = {}
    for item in input_list:
        element_list = item.strip().split('\n')
        # print('element_list = {}'.format(element_list))

        mask = element_list[0][-36:]
        # print('mask is {}'.format(mask))

        for i in element_list[1:]:
            match = pattern.match(i)
            key, value = int(match.group(1)), int(match.group(2))
            bi_value = list('{:036b}'.format(value))
            # print('bi_value = {}'.format(''.join(bi_value)))

            for k in range(36):
                if mask[k] != 'X':
                    bi_value[k] = mask[k]
            bi_value = ''.join(bi_value)
            new_int_value = int(bi_value, 2)
            # print('new_bi_value = {}'.format(bi_value)))
            element_dict[key] = new_int_value
    mem_sum = sum(element_dict.values())
    print('mem_sum is {}'.format(mem_sum))
        

if __name__  == '__main__':
    main()
