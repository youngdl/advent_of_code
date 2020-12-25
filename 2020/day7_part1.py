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

    # Find all the valid bags(with different layers)
    ini_set = {'shinygold'}
    valid_set = set()    
    while len(ini_set) != 0:
        new_set = match_set_generator(dic, ini_set)
        valid_set.update(new_set)
        ini_set = new_set
    
    print('Total Valid Number of Bags is {}'.format(len(valid_set)))


def match_set_generator(dic: dict, ini_set: set) -> set:
    new_set = set()
    if len(ini_set) != 0:
        for item in ini_set:
            for key, value in dic.items():
                if re.search(item, value):
                    new_set.add(key)
    return new_set


def key_value_generator(line: str):
    line = line.strip().replace(',', '').replace(' ', '').replace('.', '')
    key = line.split('contain')[0][:-5]
    value = line.split('contain')[1]
    return key,value
    


if __name__ == '__main__':
    main()
