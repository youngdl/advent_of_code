from typing import List, Tuple

def main():
    # read in data
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day18_data_test.txt'
    with open(file_path, 'r') as f:
        input_list = [item.strip() for item in f.readlines()]
    
    test_data = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
    top_nest_index(test_data)

def top_nest_index(formula:str) -> list:
    new_str = formula.replace(' ', '')
    line = list(new_str)
    data = Tuple[int, int, int]   #data follows the structure as (nested_level, original index from the input str, value)
    left_paren: List[data] = []
    right_paren: List[data] = []
    nest_level = 0
    for i in range(len(line)):
        if line[i] == '(':
            nest_level += 1
            left_paren.append((nest_level, i, line[i]))
        elif line[i] == ')':
            nest_level -= 1
            right_paren.append((nest_level, i, line[i]))
        
    # get the highest nested level list both on left and right parenthsis and match them
    def index(element) -> int:
        return element[1]
    nest_level_list = [item[0] for item in left_paren]
    max_nest = max(nest_level_list)
    highest_nest_list_left = [item for item in left_paren if item[0]==max_nest]
    highest_nest_list_left = sorted(highest_nest_list_left, key=index)
    
    highest_nest_list_right = [item for item in right_paren if item[0]==max_nest-1]
    highest_nest_list_right = sorted(highest_nest_list_right, key=index)

    unit: List[Tuple[int, int]] = []
    for i in range(len(highest_nest_list_left)):
        unit.append((index(highest_nest_list_left[i]), index(highest_nest_list_right[i]))) 
    
    return unit

def calculate_one_unit(one_unit: tuple, old_str: str) -> int:





if __name__ == '__main__':
    main()
