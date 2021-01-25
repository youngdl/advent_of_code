import re

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
    pattern = re.compile('^[a-z\s]+:\s(\d+)\-(\d+)\sor\s(\d+)\-(\d+)$')
    for item in field_list:
        match = pattern.match(item)
        n1 = int(match.group(1))
        n2 = int(match.group(2))
        n3 = int(match.group(3))
        n4 = int(match.group(4))
        list1 = list(range(n1,n2+1))
        list2 = list(range(n3,n4+1))
        list1.extend(list2)
        requirement_list.append(list1)

    # get the nearby ticket number
    nearby_ticket_list = [item.split(',') for item in nearby_ticket_str.split('\n')]
    
    # evaluate the validation of each nearby ticket
    error_rate = 0
    for ticket in nearby_ticket_list:
        for ticket_num in ticket:
            d = False
            for requirement in requirement_list:
                if int(ticket_num) in requirement:
                    d = True
                    break
            if d == False:
                error_rate += int(ticket_num)
    
    print('error rate ={} '.format(error_rate))


    

if __name__ == '__main__':
    main()
