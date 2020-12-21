# read in data and generate a list of all lines
file_path = '/Users/xiaolin/Documents/GitHub/advent_of_code/2020/data/day2_data.txt'
with open(file_path, 'r') as f:
    lines = f.readlines()

# parse everyline and extract useful information
valid_pw_count = 0
line_num = 0
for line in lines:
    info = line.split(' ')
    lowest_time = int(info[0].split('-')[0])
    highest_time = int(info[0].split('-')[1])
    target_letter = info[1][0]
    password = info[2][:-1]
    
    #determine whether a pw is valid, and count the valid ones
    letter_count = 0
    for letter in password:
        if letter == target_letter:
            letter_count += 1
    if lowest_time <= letter_count <= highest_time:
        valid_pw_count += 1
        print('The {}th line is valid'.format(line_num))
    line_num += 1

print('Total valid password number is {}'.format(valid_pw_count))
