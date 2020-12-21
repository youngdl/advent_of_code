# read in data and generate a list of all lines
file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day2_data.txt'
with open(file_path, 'r') as f:
    lines = f.readlines()

# parse every line and extract useful information
valid_pw_count = 0
line_num = 0
for line in lines:
    info = line.split(' ')
    position1 = int(info[0].split('-')[0])
    position2 = int(info[0].split('-')[1])
    target_letter = info[1][0]
    password = info[2][:-1]
    # determine whether the password is valid
    if password[position1-1] == target_letter and password[position2-1] != target_letter:
        valid_pw_count += 1
        print('The {}th line of password is valid'.format(line_num))
    if password[position1-1] != target_letter and password[position2-1] == target_letter:
        valid_pw_count += 1
        print('The {}th line of password is valid'.format(line_num))   
    line_num += 1

print('There are {} passwords are valid'.format(valid_pw_count))
