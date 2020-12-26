import re
def main():

    # read in the data
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day7_data.txt'
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # generate the dictionary to hold two parts of the info(container and target bag)
    dic = {}
    for line in lines:
        key, value = key_value_generator(line)
        dic[key] = value

    # search all the bags
    init_bag_list = ['shinygold']
    final_list = []
    while len(init_bag_list) != 0:
        new_list = inside_bag_list(init_bag_list, dic)
        final_list.extend(new_list)
        init_bag_list = new_list

    print('Total bag number is {}'.format(len(final_list)))


def inside_bag_list(bag_list:list, dic:dict) -> list:

    return_list = []
    for color in bag_list:
        if color in dic.keys():
            value = dic[color]
            if re.search('nobags', value):
                pass
            else:
                value_list = re.findall('\d[a-z]+', value)
                for item in value_list:
                    match_ob = re.match('^(\d)([a-z]+)bags?', item)
                    return_list.extend([match_ob.group(2)] * int(match_ob.group(1)))
        
    return return_list

            
def key_value_generator(line: str):
    line = line.strip().replace(',', '').replace(' ', '').replace('.', '')
    key = line.split('contain')[0][:-4]
    value = line.split('contain')[1]
    return key, value


if __name__ == '__main__':
    main() 
