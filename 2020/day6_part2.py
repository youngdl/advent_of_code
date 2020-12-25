import re
import functools
def main():

    # read in data
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day6_data.txt' 
    with open(file_path, 'r') as f:
        groups = f.read().strip().split('\n\n')
    
    sum_num = 0
    for group in groups:
        group_list = group.split('\n')
        sum_num += get_answer(group_list)
    
    print('Total num is {}.'.format(sum_num))


def get_answer(grouplist:list) -> int:
    
    elements_list = []
    for q in grouplist:
        element = set(list(q))
        elements_list.append(element)
    # import pdb; pdb.set_trace()
    common_set = functools.reduce(lambda a,b: a.intersection(b), elements_list)
    return len(common_set)


if __name__ == '__main__':
    main()
