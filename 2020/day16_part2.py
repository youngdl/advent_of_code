import re
import itertools

def main():
    file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day16_data.txt'
    with open(file_path, 'r') as f:
        f_str = f.read().strip()
    field_str = f_str.split('\n\n')[0]
    your_ticket_str = f_str.split('\n\n')[1].split('your ticket:')[-1].strip()
    nearby_ticket_str = f_str.split('\n\n')[2].split('nearby tickets:')[-1].strip()
    
    # get the valid range for field number
    field_list = field_str.split('\n')
    requirement_list = []
    requirement_dict = {}
    pattern = re.compile('^([a-z\s]+):\s(\d+)\-(\d+)\sor\s(\d+)\-(\d+)$')
    for item in field_list:
        match = pattern.match(item)
        n1 = int(match.group(2))
        n2 = int(match.group(3))
        n3 = int(match.group(4))
        n4 = int(match.group(5))
        name = match.group(1)
        list1 = list(range(n1,n2+1))
        list2 = list(range(n3,n4+1))
        list1.extend(list2)
        requirement_list.append(list1)
        requirement_dict[name] = list1

    requirement_set = set(requirement_dict.keys())

    # get the nearby ticket number
    nearby_ticket_list = [item.split(',') for item in nearby_ticket_str.split('\n')]

    # evaluate the validation of each nearby ticket
    def _isvalid(ticket:list, requirement_list:list) -> bool: 
        
        for ticket_num in ticket:
            d = False
            for requirement in requirement_list:
                if int(ticket_num) in requirement:
                    d = True
                    break
            if d == False:
                return False
        return True
    
    valid_ticket = [ticket for ticket in nearby_ticket_list if _isvalid(ticket, requirement_list)]


    # generate a dictionary to store how many possible fields one line could be
    key_dict = {}
    for i in range(len(valid_ticket[0])):
        element = [int(item[i]) for item in valid_ticket]
        key_list = []
        for item in requirement_list:
            if set(element).issubset(set(item)):
                key = list(requirement_dict.keys())[list(requirement_dict.values()).index(item)]
                key_list.append(key)
        key_dict[i] = key_list

    # get the only possible field arrangement from all the valid tickets    
    sort_field = sorted(key_dict.items(), key=lambda field: len(field[-1]))
    for item in sort_field:
        field = set(item[-1]) & requirement_set
        key_dict[item[0]] = field
        requirement_set = requirement_set - field
    
    # extract field with departure at the begining
    departure_list = []
    for item in key_dict.items():
        d_pattern = re.compile('^departure')
        d_match = d_pattern.match(list(item[-1])[0])
        if d_match:
            departure_list.append(item[0])

    # Calculate the final muplicaton
    result = 1
    for i in departure_list:
        result *= int(your_ticket_str.split(',')[i])
    print('The multiplication is {}'.format(result))

if __name__ == '__main__':
    main()
